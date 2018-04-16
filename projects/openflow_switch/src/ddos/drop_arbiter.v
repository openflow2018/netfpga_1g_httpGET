module drop_arbiter
	#(
      parameter MAX_DEPTH_BITS_BLACKLIST = 14
    )
(
	//-- interface to modifidied header parser
	input [31:0] 					src_ip,
	input							hash2_vld,
	input [MAX_DEPTH_BITS_BLACKLIST-1:0] addr2_hash,
	input 							is_pkt_arp, 	

	// -- interface to hash table
	input [31:0]					src_ip_drop,
	input							drop_pkt,				

	//-- interface to opl_processor
    input 							header_fifo_rd_en,
    output[1:0]						header_fifo_dout,
    output 							header_fifo_empty,

    output reg						header_fifo_wr_en,
    output reg[1:0]					header_fifo_din,						

	// -- Misc
	input 							clk, reset,

	//-- check out
	output reg[1:0]					state_drop,
	output [31:0] 					data_from_bram2,
	output[MAX_DEPTH_BITS_BLACKLIST-1:0] 		addr_bram2,

	//-- test write regs
	input[31:0]						test_flush


	);

small_fifo
	#(.WIDTH(2),
	 .MAX_DEPTH_BITS(1))
	small_fifo_is_drop
	  (.din           (header_fifo_din),     // Data in
	   .wr_en         (header_fifo_wr_en),   // Write enable

	   .rd_en         (header_fifo_rd_en),   // Read the next word
	   .dout          (header_fifo_dout),
	   
	   .full          (),
	   .nearly_full   (),
	   .prog_full   (),
	   .empty         (header_fifo_empty),
	   .reset         (reset),
	   .clk           (clk)
	   );

//-- clock 10s
reg flush_t;
// wire[MAX_DEPTH_BITS-1:0] addr_bram2;
reg[MAX_DEPTH_BITS_BLACKLIST-1:0] addr_flush;
reg is_FLUSH_BLACK_LIST;
wire[31:0] in_data_bram2;
wire wr_en_bram2;



BRAM2 
	BRAM2
	(
		.clk(clk),
		.wr_en(wr_en_bram2),
		.in_data(in_data_bram2),    // udpate_hash_table -> bram
		.addr(addr_bram2),
		.out_data(data_from_bram2)     // bram -> update_hash_table
		);

localparam IDLE = 0;
localparam LOOKUP = 1;
localparam ARP_PACKET = 2;
localparam FLUSH_BLACK_LIST = 3;


assign addr_bram2 = is_FLUSH_BLACK_LIST ? addr_flush : addr2_hash;
assign in_data_bram2 = is_FLUSH_BLACK_LIST ? 0 : src_ip_drop;
assign wr_en_bram2 = is_FLUSH_BLACK_LIST ? 1 : drop_pkt ;

//------------------------------------------------------
always @(posedge clk) begin
	if (reset) begin
		state_drop <= IDLE;
		header_fifo_wr_en <= 0;
		header_fifo_din <= 0;
		is_FLUSH_BLACK_LIST <= 0;
		addr_flush <= 0;
	end
	else begin
		header_fifo_wr_en <= 0;
		header_fifo_din <= 0;
		is_FLUSH_BLACK_LIST <= 0;

		case (state_drop)
			IDLE: begin
				if (flush_t && (test_flush == 3)) begin
					state_drop <= FLUSH_BLACK_LIST;
					addr_flush <= 0;
				end
				if (test_flush == 5) begin
					state_drop <= FLUSH_BLACK_LIST;
					addr_flush <= 0;
				end
				else if(is_pkt_arp) begin
					state_drop <= ARP_PACKET;
				end
				else if (hash2_vld) begin
					state_drop <= LOOKUP;
				end
			end			
			LOOKUP: begin
				header_fifo_wr_en <= 1;
				if (src_ip == data_from_bram2) begin
					header_fifo_din <= 2'b11;
				end
				else begin
					header_fifo_din <= 2'b01;
				end
				state_drop <= IDLE;
			end
			ARP_PACKET: begin
				header_fifo_wr_en <= 1;
				header_fifo_din <= 2'b10;
				state_drop <= IDLE;
			end
			FLUSH_BLACK_LIST: begin
				is_FLUSH_BLACK_LIST <= 1;
				if (is_pkt_arp || hash2_vld) begin
					header_fifo_wr_en <= 1;
					header_fifo_din <= 2'b01;
				end
				if(addr_flush=={MAX_DEPTH_BITS_BLACKLIST{1'b1}}) begin
				// if(addr_flush==200) begin
					state_drop <= IDLE;
					addr_flush <= 0;
				end
				else begin
					addr_flush <= addr_flush + 1;
				end		
			end
		endcase
	end
end


//-- clock 60s
localparam MAX_CLOCK = 7500000000; // 60s
integer count_fl;

always @(posedge clk) begin
	if (reset) begin
		count_fl <= 0;		
		flush_t <= 0;
	end
	else begin
		count_fl <= count_fl + 1;
		if (count_fl == MAX_CLOCK) begin
			flush_t <= 1;													
		end
		if (count_fl == MAX_CLOCK+5) begin
			count_fl <= 0;
			flush_t <= 0;
		end
	end
end

endmodule

