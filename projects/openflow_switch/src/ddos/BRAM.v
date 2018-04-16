
module BRAM
	#(
	  parameter BRAM_WIDTH = 37,
      parameter MAX_DEPTH_BITS = 14,
      parameter TOTAL_NUM = 2**MAX_DEPTH_BITS
	  )
	(
	input clk,
	input wr_en,
	input [BRAM_WIDTH-1:0] in_data,
	input [MAX_DEPTH_BITS-1:0] addr,

	output reg  [BRAM_WIDTH-1:0] out_data
	);

reg [BRAM_WIDTH-1:0] reg_array [TOTAL_NUM-1:0];

integer i;

// initial begin
//     for( i = 0; i < TOTAL_NUM; i = i + 1 ) begin
//         reg_array[i] <= 0;
//     end
// end

always @(posedge clk) begin
	if(wr_en)
		reg_array[addr] <= in_data; 	
		
	out_data <= reg_array[addr];

end

endmodule




