`include "registers.v"

module top_ddos
	#(
	  parameter BRAM_WIDTH 				= 37,
      parameter MAX_DEPTH_BITS_HASH_TABLE	= 14,
      parameter MAX_DEPTH_BITS_BLACKLIST    = 14,
      parameter UDP_REG_SRC_WIDTH 		= 2
    )
(
	// -- Misc
	input                                 clk, 
	input 								  reset,
	output 								  flush_1s,

	// -- interface to modified_header_parser
    input [31:0]                      	src_ip,
    input [MAX_DEPTH_BITS_HASH_TABLE-1:0]   addr_hash,
    input                             	hash_vld,
    input								hash2_vld,
    input[MAX_DEPTH_BITS_BLACKLIST-1:0]	addr2_hash,
    input 								is_pkt_arp,

    // -- interface to opl_processor
    input 								  header_fifo_rd_en,
    output[1:0]							  header_fifo_dout,
    output 								  header_fifo_empty,
    output[1:0]							  header_fifo_din,
    output								  header_fifo_wr_en,


    // --Registers interface:
    input                                   reg_req_in,
	input                                   reg_ack_in,
	input                                   reg_rd_wr_L_in,
	input  [`UDP_REG_ADDR_WIDTH-1:0]        reg_addr_in,
	input  [`CPCI_NF2_DATA_WIDTH-1:0]       reg_data_in,
	input  [UDP_REG_SRC_WIDTH-1:0]          reg_src_in,

	output                                  reg_req_out,
	output                                  reg_ack_out,
	output                                  reg_rd_wr_L_out,
	output  [`UDP_REG_ADDR_WIDTH-1:0]       reg_addr_out,
	output  [`CPCI_NF2_DATA_WIDTH-1:0]      reg_data_out,
	output  [UDP_REG_SRC_WIDTH-1:0]         reg_src_out,


    // -- check out 
    output[1:0]					   	  	  state, // hash_table state
    output[31:0] 						  src_ip_drop,
	output								  drop_pkt,
	output[BRAM_WIDTH-1:0] 				  in_data_bram, 
	output[BRAM_WIDTH-1:0] 				  out_data_bram,

	output								  is_FLUSH_TABLE,

	output[1:0] 						  state_drop,
	output[31:0]						  data_from_bram2,
	output[MAX_DEPTH_BITS_HASH_TABLE-1:0]						  addr_bram,
	output[MAX_DEPTH_BITS_BLACKLIST-1:0] 						  addr_bram2
);


wire 									  wr_en; //--> BRAM
wire[31:0] control_reg;
wire[31:0] max_count;
wire[31:0] ddos_threshold;
wire flush_t;

hash_table
	hash_table
	(	
	// interface to header_parser
		.src_ip(src_ip),
		.hash_vld(hash_vld),
		.flush_1s(flush_1s),
		.addr_hash(addr_hash),
	
	//	interface to BRAM
		.in_data_bram(in_data_bram),
		.wr_en(wr_en),
		// .addr_flush(addr_flush), //--> reset BRAM
		.out_data_bram(out_data_bram),
		.addr_bram(addr_bram),

	// output
		.src_ip_drop(src_ip_drop),
		.drop_pkt(drop_pkt),
		.is_FLUSH_TABLE(is_FLUSH_TABLE),

	// Misc
		.clk(clk),
		.reset(reset),

	// check out
		.state(state),
		.max_count(max_count),
		.ddos_threshold(ddos_threshold)
	);


drop_arbiter
	drop_arbiter
	(
		//-- interface to modifidied header parser
		.src_ip(src_ip),
		.hash2_vld(hash2_vld),
		.addr2_hash(addr2_hash),
		.is_pkt_arp(is_pkt_arp),

		// -- interface to hash table
		.src_ip_drop(src_ip_drop),
		.drop_pkt(drop_pkt),

		//-- interface to opl_processor
		.header_fifo_rd_en(header_fifo_rd_en),
		.header_fifo_dout(header_fifo_dout),
		.header_fifo_empty(header_fifo_empty),
		
		.header_fifo_wr_en(header_fifo_wr_en),
		.header_fifo_din(header_fifo_din),

		// -- Misc
		.clk(clk),
		.reset(reset),

		// -- check out
		.state_drop(state_drop),
		.data_from_bram2(data_from_bram2),
		.addr_bram2(addr_bram2),

		//-- test write regs
		.test_flush(control_reg)
	);



generic_regs
   #( 
      .UDP_REG_SRC_WIDTH   (UDP_REG_SRC_WIDTH),
      .TAG                 (`TOP_DDOS_BLOCK_ADDR),
      .REG_ADDR_WIDTH      (`TOP_DDOS_REG_ADDR_WIDTH),    // Width of block addresses
      .NUM_COUNTERS        (0),                       // How many counters
      .NUM_SOFTWARE_REGS   (3),                       // How many sw regs
      .NUM_HARDWARE_REGS   (4)                        // How many hw regs        --- 96bits
   ) generic_regs (
      // for show REG
      .reg_req_in       (reg_req_in),
      .reg_ack_in       (reg_ack_in),
      .reg_rd_wr_L_in   (reg_rd_wr_L_in),
      .reg_addr_in      (reg_addr_in),
      .reg_data_in      (reg_data_in),
      .reg_src_in       (reg_src_in),

      .reg_req_out      (reg_req_out),
      .reg_ack_out      (reg_ack_out),
      .reg_rd_wr_L_out  (reg_rd_wr_L_out),
      .reg_addr_out     (reg_addr_out),
      .reg_data_out     (reg_data_out),
      .reg_src_out      (reg_src_out),

      // --- counters interface
      .counter_updates  (),
      .counter_decrement(),

      // --- SW regs interface
      .software_regs    ({control_reg, max_count, ddos_threshold}),
 
      .hardware_regs ({src_ip_drop, out_data_bram[36:5], 27'b0, out_data_bram[4:0], 31'b0, flush_1s}),

      .clk              (clk),
      .reset            (reset)
    );

endmodule