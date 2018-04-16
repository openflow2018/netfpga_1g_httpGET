module hash_table
	#(
	  parameter BRAM_WIDTH = 37, // src_IP (32), count (5)
      parameter MAX_DEPTH_BITS_HASH_TABLE = 14
      // parameter DDOS_THRESHOLD = 8	
    )
(
	// interface to header_parser
    input[31:0]                                   src_ip,
    input                                         hash_vld, 
    output reg									  flush_1s,
    input [MAX_DEPTH_BITS_HASH_TABLE-1:0]        			  addr_hash,
                               
	/*
	interface to BRAM
	*/
	output [BRAM_WIDTH-1:0]                        in_data_bram,
	output reg                                    wr_en,
   	output wire[MAX_DEPTH_BITS_HASH_TABLE-1:0]  		  			  addr_bram,
	output [BRAM_WIDTH-1:0]                       out_data_bram,

	// output
	output reg[31:0]                              src_ip_drop,
	output reg                                    drop_pkt, 
	output reg 									  is_FLUSH_TABLE,

	// -- Misc
	input                                         clk, 
	input 										  reset,

	// check out
    output reg [1:0] 							  state,
    input[31:0] 								  max_count,
    input[31:0]									  ddos_threshold
);

	localparam IDLE 			            = 0;
    localparam UPDATE_TABLE                 = 1;
    localparam FLUSH_TABLE					= 2;
    localparam NOT_GET_PKT 					= 3; 

    wire[31:0] src_ip_1;
    wire[4:0] count_1;

    reg[31:0] src_ip_1_update;
    reg[4:0] count_1_update;
   	// wire[MAX_DEPTH_BITS-1:0]  		  addr_bram;

BRAM 
	BRAM
	(
		.clk(clk),
		.wr_en(wr_en),
		.in_data(out_data_bram),    // udpate_hash_table -> bram
		.addr(addr_bram),
		.out_data(in_data_bram)     // bram -> update_hash_table
		);

reg [MAX_DEPTH_BITS_HASH_TABLE-1:0] 				  addr_flush;
assign addr_bram = is_FLUSH_TABLE ? addr_flush : addr_hash;

assign out_data_bram = {src_ip_1_update,count_1_update};
assign src_ip_1 = in_data_bram[36:5];
assign count_1 = in_data_bram[4:0];

	always @(posedge clk) begin
		if (reset) begin
			state <= IDLE;
			wr_en <= 0;
			//

			src_ip_1_update <= 0;
			count_1_update <= 0;

			//
			src_ip_drop <= 0;
			drop_pkt <= 0;
			is_FLUSH_TABLE <= 0;
			//
			addr_flush <= 0;
		end
		else begin
			wr_en <= 0;
			is_FLUSH_TABLE <= 0;

			case(state)
				IDLE: begin
					wr_en <= 0;
					drop_pkt <= 0;
					
					if(flush_1s) begin
						state <= FLUSH_TABLE;
						addr_flush <= 0;
					end
					else if(hash_vld) begin
						state <= UPDATE_TABLE;
					end
				end

				UPDATE_TABLE: begin
					wr_en <= 1;
					// same IP
					if(src_ip == src_ip_1) begin
						if(count_1 >= ddos_threshold) begin
							src_ip_drop <= src_ip_1;
							drop_pkt <= 1;							
		                    count_1_update <= count_1;
		                    src_ip_1_update <= src_ip_1;
						end
						else begin

		                    count_1_update <= count_1 + 1;
		                    src_ip_1_update <= src_ip_1;
		                end
		            end
					// different IP
					// else if((src_ip != src_ip_1) && (count_1 <= 1)) begin 
					else if (((src_ip != src_ip_1) && (count_1 <= 1))||(count_1 >= ddos_threshold)) begin
		               src_ip_1_update <= src_ip;
		               count_1_update <= 1;
		            end
					state <= IDLE;
				end
				FLUSH_TABLE: begin
					is_FLUSH_TABLE <= 1;
					wr_en 	 <= 1;
					if(addr_flush=={MAX_DEPTH_BITS_HASH_TABLE{1'b1}}) begin
					// if(addr_flush==100) begin
						state <= IDLE;
						wr_en <= 0;
						addr_flush <= 0;
					end
					else begin
						addr_flush <= addr_flush + 1;
						src_ip_1_update <= 0;
						count_1_update <= 0;
					end
				end
			endcase
		end
	end


//-- clock 1s
// localparam MAX_CLOCK = 125000000;
integer count_fl;

always @(posedge clk) begin
	if (reset) begin
		count_fl <= 0;		
		flush_1s <= 0;
	end
	else begin
		count_fl <= count_fl + 1;
		// if (count_fl == MAX_CLOCK) begin
		if(count_fl == max_count) begin
			flush_1s <= 1;													
		end
		// if (count_fl == MAX_CLOCK+10) begin
		if(count_fl == max_count+10) begin 
			count_fl <= 0;
			flush_1s <= 0;
		end
	end
end

endmodule
