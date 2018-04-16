///////////////////////////////////////////////////////////////////////////////
// $Id$
//
// Module: header_parser.v
// Project: NF2.1 OpenFlow Switch
// Author: Jad Naous <jnaous@stanford.edu>
// Description: gets a flow entry to match against
// The module parses a vanilla IP pkt with no VLAN or SNAP hdr. The parameter
// additional word can be used to add a word to the flow entry from a
// module header such as a VLAN ID. IP options are handled.
//
// An additional word can be added to the flow header from a module header. The
// following parameters specify where and how:
// - ADDITIONAL_WORD_SIZE: number of bits to use from the module header and add
//                         to flow header
// - ADDITIONAL_WORD_BITMASK: This is ANDed with the word
// - ADDITIONAL_WORD_POS: Where to put the word in the flow header
// - ADDITIONAL_WORD_CTRL: Specifies which module header to use
// - ADDITIONAL_WORD_DEFAULT: default value if no matching module header found
//
// - This module complies with OpenFlow v1.0.
//   As of v1.0, IP_TOS matching field is added, and IP_SRC, IP_DST, IP_PROTO
//   fields are also used for ARP matching.
//
// Licensing: In addition to the NetFPGA license, the following license applies
//            to the source code in the OpenFlow Switch implementation on NetFPGA.
//
// Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
//
// We are making the OpenFlow specification and associated documentation (Software)
// available for public use and benefit with the expectation that others will use,
// modify and enhance the Software and contribute those enhancements back to the
// community. However, since we would like to make the Software available for
// broadest use, with as few restrictions as possible permission is hereby granted,
// free of charge, to any person obtaining a copy of this Software to deal in the
// Software under the copyrights without restriction, including without limitation
// the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
// sell copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//
// The name and trademarks of copyright holder(s) may NOT be used in advertising
// or publicity pertaining to the Software or any derivatives without specific,
// written prior permission.
///////////////////////////////////////////////////////////////////////////////
`include "crc_func_0_d256.v"
`include "registers.v"
`include "ip_hash.v"

  module header_parser
    #(parameter DATA_WIDTH                  = 64,
      parameter CTRL_WIDTH                  = DATA_WIDTH/8,
      parameter PKT_SIZE_WIDTH              = 12,
      parameter ADDITIONAL_WORD_SIZE        = 16,
      parameter ADDITIONAL_WORD_BITMASK     = 16'h0fff,
      parameter ADDITIONAL_WORD_POS         = 224,
      parameter ADDITIONAL_WORD_CTRL        = 8'h40,
      parameter ADDITIONAL_WORD_DEFAULT     = 16'hffff,
      parameter FLOW_ENTRY_SIZE             = 240,

      parameter IOQ_SRC_PORT_POS            = 16,
      parameter IOQ_BYTE_LEN_POS            = 0,

      // hash function
      parameter MAX_DEPTH_BITS_HASH_TABLE              = 14,
      parameter MAX_DEPTH_BITS_BLACKLIST = 14,
      parameter IN_HASH_WIDTH               = 256
      )
   (// --- Interface to the previous stage
    input  [DATA_WIDTH-1:0]                in_data,
    input  [CTRL_WIDTH-1:0]                in_ctrl,
    input                                  in_wr,

    // --- Interface to matchers
    output reg [FLOW_ENTRY_SIZE-1:0]       flow_entry,
    output [`OPENFLOW_ENTRY_SRC_PORT_WIDTH-1:0] flow_entry_src_port,
    output reg [PKT_SIZE_WIDTH-1:0]        pkt_size,
    output reg                             flow_entry_vld,

    // --- Misc
    input                                  reset,
    input                                  clk,

    // --- interface to top_ddos
    output reg [31:0]                      src_ip,
    output reg [MAX_DEPTH_BITS_HASH_TABLE-1:0] addr_hash,
    output reg                             hash_vld,
    output reg                             is_pkt_arp,

    // -- interface to drop_arbiter
    output reg [MAX_DEPTH_BITS_BLACKLIST-1:0] addr2_hash,
    output reg                             hash2_vld,

    // check out signals
    output   reg [IN_HASH_WIDTH-1:0]       in_data_hash,
    output wire[5:0]                       counter_check,
    output reg                             is_arp,
    output wire[1:0]                       state_header

   );

   //`LOG2_FUNC
   `CRC_FUNC_0
   `CRC_FUNC_1   

   //------------------ Internal Parameter ---------------------------
   localparam MODULE_HDRS                   = 0;
   localparam PKT_WORDS                     = 1;
   localparam WAIT_EOP                      = 2;
   localparam RESET_FLOW_ENTRY              = 3;

   localparam MAC_SRC_LO_ETHERTYPE_WORD     = 1,
              IP_PROT_WORD                  = 2,
              IP_SRC_DST_HI_WORD            = 3,
              IP_DST_LO_TRANSP_PORTS_WORD   = 4,
              ARP_DST_HI_WORD               = 5,
              ARP_DST_LO_WORD               = 6,
              CHECK_TCP_LEN                 = 7, 
              WORD_7                        = 8,
              WORD_8                        = 9,
              WORD_9                        = 10,
              WORD_10                       = 11,
              WORD_11                       = 12,
              WORD_12                       = 13,
              WORD_13                       = 14,
              WORD_14                       = 15,
              WORD_15                       = 16,
              WORD_16                       = 17,
              WORD_17                       = 18,
              WORD_18                       = 19,
              WORD_19                       = 20,
              WORD_20                       = 21,
              WORD_21                       = 22,
              WORD_22                       = 23,
              WORD_23                       = 24,
              WORD_24                       = 25,
              WORD_25                       = 26,
              WORD_26                       = 27,
              WORD_27                       = 28; //state for calculate HASH_FUNCTION

   //---------------------- Wires/Regs -------------------------------
   reg [1:0]                            state;
   assign state_header = state;
   reg [5:0]                            counter; // store more words
   assign counter_check = counter ;

   reg                                  is_ip;
   reg                                  is_tcp_udp;
   reg                                  is_icmp;
   reg                                  is_vlan;
   // reg                                  is_arp;

   reg [3:0]                            ip_hdr_len;
   wire [FLOW_ENTRY_SIZE-1:0]           flow_entry_default;
   /*
    Additional signal for URL Extract
    */
   reg                                    win_pkt;
   wire [3:0]                             tcp_hdr_len;
   //wire [7:0]                             ip_proto;
   //wire [15:0]                            ip_len;
   wire [15:0]                            dst_port;
   wire [15:0]                            req_meth_win;
   wire [23:0]                            req_meth_unix;
   wire [47:0]                            URL_win;
   wire [15:0]                            URL_unix;
   reg                                    is_get_pkt_unix,is_get_pkt_win;
   //
   reg [31:0] dst_ip;

   localparam HTTP               = 16'h0050;    // port 80
   localparam SP                 = 8'h20;
   localparam WIN_TCP_HDR_LEN    = 4'b0101;     // 5 * 32b = 20B
   localparam GE                 = 16'h4745;    // "GE"
   localparam GET                = 24'h474554;  // "GET"

   assign req_meth_unix = in_data[47:24];  
   assign req_meth_win = in_data[15:0];  
   //assign ip_proto = in_data[7:0];
   //assign ip_len = in_data[63:48];
   assign dst_port = in_data[31:16];
   assign tcp_hdr_len = in_data[15:12];
   //extract
   assign URL_win = in_data[47:0];
   assign URL_unix = in_data[15:0];

  //=============================== HASH FUNCTION ========================================================

   /* Check for postion of URL*/
  wire is_sp;
  wire is_sp_win_word8, is_sp_linux_word9;

  assign is_sp = ((in_data[63:56]==8'h20)||(in_data[55:48]==8'h20)||(in_data[47:40]==8'h20)
                 ||(in_data[39:32]==8'h20)||(in_data[31:24]==8'h20)||(in_data[23:16]==8'h20)
                 ||(in_data[15:8]==8'h20)||(in_data[7:0]==8'h20));

  assign is_sp_win_word8 = ((in_data[39:32]==8'h20)||(in_data[31:24]==8'h20)||(in_data[23:16]==8'h20)
                 ||(in_data[15:8]==8'h20)||(in_data[7:0]==8'h20));
  assign is_sp_linux_word9 = in_data[7:0]==8'h20;

  // MASK 
  wire [7:0] byte_0, byte_1,byte_2,byte_3,byte_4,byte_5,byte_6,byte_7;
  wire [7:0] mask_0, mask_1, mask_2, mask_3, mask_4, mask_5, mask_6, mask_7;
  wire [63:0] mask_URI;

  assign byte_0 = in_data[7:0] ;
  assign byte_1 = in_data[15:8] ;
  assign byte_2 = in_data[23:16] ;
  assign byte_3 = in_data[31:24] ;
  assign byte_4 = in_data[39:32] ;
  assign byte_5 = in_data[47:40] ;
  assign byte_6 = in_data[55:48] ;
  assign byte_7 = in_data[63:56] ;

  assign mask_0 = (byte_7==SP) ? 0 : 
                  (byte_6==SP) ? 0 :
                  (byte_5==SP) ? 0 :
                  (byte_4==SP) ? 0 : 
                  (byte_3==SP) ? 0 :
                  (byte_2==SP) ? 0 :
                  (byte_1==SP) ? 0 :
                  (byte_0==SP) ? 0 : 8'hFF;
  assign mask_1 = (byte_7==SP) ? 0 : 
                  (byte_6==SP) ? 0 :
                  (byte_5==SP) ? 0 :
                  (byte_4==SP) ? 0 : 
                  (byte_3==SP) ? 0 :
                  (byte_2==SP) ? 0 :
                  (byte_1==SP) ? 0 : 8'hFF;
  assign mask_2 = (byte_7==SP) ? 0 : 
                  (byte_6==SP) ? 0 :
                  (byte_5==SP) ? 0 :
                  (byte_4==SP) ? 0 : 
                  (byte_3==SP) ? 0 :
                  (byte_2==SP) ? 0 : 8'hFF;
  assign mask_3 = (byte_7==SP) ? 0 : 
                  (byte_6==SP) ? 0 :
                  (byte_5==SP) ? 0 :
                  (byte_4==SP) ? 0 : 8'hFF;
  assign mask_4 = (byte_7==SP) ? 0 : 
                  (byte_6==SP) ? 0 :
                  (byte_5==SP) ? 0 :
                  (byte_4==SP) ? 0 : 8'hFF;
  assign mask_5 = (byte_7==SP) ? 0 : 
                  (byte_6==SP) ? 0 :
                  (byte_5==SP) ? 0 : 8'hFF;
  assign mask_6 = (byte_7==SP) ? 0 : 
                  (byte_6==SP) ? 0 : 8'hFF;
  assign mask_7 = (byte_7==SP) ? 0 : 8'hFF;

  assign mask_URI = {mask_7, mask_6, mask_5, mask_4, mask_3, mask_2, mask_1, mask_0};



   //------------------------ Logic ----------------------------------
   assign flow_entry_src_port = flow_entry[`OPENFLOW_ENTRY_SRC_PORT_POS + `OPENFLOW_ENTRY_SRC_PORT_WIDTH - 1 : `OPENFLOW_ENTRY_SRC_PORT_POS];
   generate
      if(FLOW_ENTRY_SIZE > ADDITIONAL_WORD_POS+ADDITIONAL_WORD_SIZE) begin:gen_flow_msb
         assign flow_entry_default[FLOW_ENTRY_SIZE-1:ADDITIONAL_WORD_POS+ADDITIONAL_WORD_SIZE]     = 0;
      end
   endgenerate
   assign flow_entry_default[ADDITIONAL_WORD_POS+ADDITIONAL_WORD_SIZE-1:ADDITIONAL_WORD_POS] = ADDITIONAL_WORD_DEFAULT;
   assign flow_entry_default[ADDITIONAL_WORD_POS-1:0]                                        = 0;

   /* This state machine parses the header */
   always @(posedge clk) begin
      if(reset) begin
         counter           <= 0;
         flow_entry_vld    <= 0;
         flow_entry        <= flow_entry_default;
         pkt_size          <= 0;
         state             <= MODULE_HDRS;
         is_ip             <= 0;
         is_tcp_udp        <= 0;
         is_icmp           <= 0;
         is_vlan           <= 0;
         ip_hdr_len        <= 0;
         is_arp             <= 0;
         // addition
         win_pkt <= 0;
         is_get_pkt_win <= 0;
         is_get_pkt_unix <= 0;
         //
         in_data_hash <= 0;
         addr_hash <= 0;
         src_ip <= 0;
         dst_ip <= 0;
         hash_vld <= 0;
         is_pkt_arp <= 0;

        //- bram2
        addr2_hash <= 0;
        hash2_vld <= 0;
      end

      else begin
         flow_entry_vld    <= 0;
         //
         hash_vld <= 0;
         is_pkt_arp <= 0;

         // - bram2
         hash2_vld <= 0;

         case (state)
            RESET_FLOW_ENTRY: begin
               flow_entry    <= flow_entry_default;
               state         <= MODULE_HDRS;
               if(in_wr) begin
                  // check for the additional word
                  if(in_ctrl==ADDITIONAL_WORD_CTRL) begin
                     flow_entry[ADDITIONAL_WORD_POS + ADDITIONAL_WORD_SIZE - 1 : ADDITIONAL_WORD_POS]
                                                      <= in_data[ADDITIONAL_WORD_SIZE-1 : 0] & ADDITIONAL_WORD_BITMASK;
                     is_vlan <= (in_ctrl==`VLAN_CTRL_WORD);
                  end
                  // get the pkt size and the input port
                  else if(in_ctrl==`IO_QUEUE_STAGE_NUM) begin
                     flow_entry[`OPENFLOW_ENTRY_SRC_PORT_POS + `OPENFLOW_ENTRY_SRC_PORT_WIDTH - 1 : `OPENFLOW_ENTRY_SRC_PORT_POS]
                                                          <= in_data[IOQ_SRC_PORT_POS + `OPENFLOW_ENTRY_SRC_PORT_WIDTH - 1 : IOQ_SRC_PORT_POS];
                     if(is_vlan) begin
                        pkt_size <= (in_data[IOQ_BYTE_LEN_POS + PKT_SIZE_WIDTH - 1:IOQ_BYTE_LEN_POS] + 4);
                     end
                     else begin
                        pkt_size <= in_data[IOQ_BYTE_LEN_POS + PKT_SIZE_WIDTH - 1:IOQ_BYTE_LEN_POS];
                     end
                     is_vlan <= 0;
                  end
                  // pkt should not be started
                  // synthesis translate_off
                  else if(in_ctrl==0) begin
                     $display("%t %m ERROR: found ctrl=0 as first word of pkt.", $time);
                     $stop;
                  end
                  // synthesis translate_on
               end // if (in_wr)
            end // case: RESET_FLOW_ENTRY

            MODULE_HDRS: begin
               if(in_wr) begin
                  // check for the additional word
                  if(in_ctrl==ADDITIONAL_WORD_CTRL) begin
                     flow_entry[ADDITIONAL_WORD_POS + ADDITIONAL_WORD_SIZE - 1 : ADDITIONAL_WORD_POS]
                                                      <= in_data[ADDITIONAL_WORD_SIZE-1 : 0] & ADDITIONAL_WORD_BITMASK;
                     is_vlan <= (in_ctrl==`VLAN_CTRL_WORD);
                  end
                  // get the pkt size and the input port
                  else if(in_ctrl==`IO_QUEUE_STAGE_NUM) begin
                     flow_entry[`OPENFLOW_ENTRY_SRC_PORT_POS + `OPENFLOW_ENTRY_SRC_PORT_WIDTH - 1:`OPENFLOW_ENTRY_SRC_PORT_POS]
                                                          <= in_data[IOQ_SRC_PORT_POS + `OPENFLOW_ENTRY_SRC_PORT_WIDTH - 1:IOQ_SRC_PORT_POS];
                     if(is_vlan) begin
                        pkt_size <= (in_data[IOQ_BYTE_LEN_POS + PKT_SIZE_WIDTH - 1:IOQ_BYTE_LEN_POS] + 4);
                     end
                     else begin
                        pkt_size <= in_data[IOQ_BYTE_LEN_POS + PKT_SIZE_WIDTH - 1:IOQ_BYTE_LEN_POS];
                     end
                     is_vlan <= 0;
                  end
                  // pkt started - get MAC dst and src hi
                  else if(in_ctrl==0) begin
                     flow_entry[`OPENFLOW_ENTRY_ETH_DST_POS + 47 : `OPENFLOW_ENTRY_ETH_DST_POS]
                                        <= in_data[63:16];

                     flow_entry[`OPENFLOW_ENTRY_ETH_SRC_POS + 47 : `OPENFLOW_ENTRY_ETH_SRC_POS + 32]
                                        <= in_data[15:0];
                     state    <= PKT_WORDS;
                  end
                  counter <= 1;
               end // if (in_wr)
            end // case: MODULE_HDRS

            PKT_WORDS: begin
               if(in_wr) begin

                  counter <= counter + 1;

                  case(counter)
                     MAC_SRC_LO_ETHERTYPE_WORD: begin
                        flow_entry[`OPENFLOW_ENTRY_ETH_SRC_POS + 31 : `OPENFLOW_ENTRY_ETH_SRC_POS]
                                                        <= in_data[63:32];

                        flow_entry[`OPENFLOW_ENTRY_ETH_TYPE_POS + 15 : `OPENFLOW_ENTRY_ETH_TYPE_POS]
                                                        <= in_data[31:16];

                        if (in_data[31:16] == `ETH_TYPE_IP) begin
                           flow_entry[`OPENFLOW_ENTRY_IP_TOS_POS + 7 : `OPENFLOW_ENTRY_IP_TOS_POS + 2]
                                                           <= in_data[7:2];
                        end

                        is_ip      <= in_data[31:16] == `ETH_TYPE_IP;
                        is_arp     <= in_data[31:16] == `ETH_TYPE_ARP;
                        ip_hdr_len <= in_data[11:8];
                     end

                     IP_PROT_WORD: begin
                        if(is_ip) begin
                           flow_entry[`OPENFLOW_ENTRY_IP_PROTO_POS + 7 : `OPENFLOW_ENTRY_IP_PROTO_POS] <= in_data[7:0];
                           /* check validity of hdr length field */
                           if(ip_hdr_len < 5) begin
                              flow_entry        <= flow_entry_default;
                              flow_entry_vld    <= 1'b1;
                              state             <= WAIT_EOP;
                           end
                        end
                        else if(is_arp) begin
                           flow_entry[`OPENFLOW_ENTRY_IP_PROTO_POS + 7 : `OPENFLOW_ENTRY_IP_PROTO_POS] <= in_data[23:16];
                           // is_pkt_arp <= 1;
                        end
                        is_tcp_udp <= is_ip && ((in_data[7:0] == `IP_PROTO_TCP)
                                                || (in_data[7:0] == `IP_PROTO_UDP));
                        is_icmp    <= is_ip && (in_data[7:0] == `IP_PROTO_ICMP);
                     end

                     IP_SRC_DST_HI_WORD: begin   // word 4 --> src IP
                        if(is_ip) begin
                           flow_entry[`OPENFLOW_ENTRY_IP_SRC_POS + 31:`OPENFLOW_ENTRY_IP_SRC_POS]
                                <= in_data[47:16];
                           flow_entry[`OPENFLOW_ENTRY_IP_DST_POS + 31: `OPENFLOW_ENTRY_IP_DST_POS + 16]
                                <= in_data[15:0];
                        /* for Hash function */
                            src_ip <= in_data[47:16];
                            dst_ip[31:16] <= in_data[15:0];
                        /* for hash looking up in Black list */
                            hash2_vld <= 1;
                            addr2_hash <= crc_func_1({in_data[47:16],in_data[47:16]},in_data[47:16]);
                        end
                        //
                        else if(is_arp) begin
                           counter <= counter + 2; // jump to ARP_DST_HI_WORD state
                           flow_entry[`OPENFLOW_ENTRY_IP_SRC_POS + 31:`OPENFLOW_ENTRY_IP_SRC_POS]
                                <= in_data[31:0];
                           is_pkt_arp <= 1;
                        end
                        else begin
                           is_pkt_arp <= 1;
                        end
                        /* for hash looking up in Black list */
                            // is_pkt_arp <= 1;
                        
                     end

                     IP_DST_LO_TRANSP_PORTS_WORD: begin
                        counter       <= counter; // stay in this state to get tcp/udp ports
                        ip_hdr_len    <= ip_hdr_len - 2'h2; // keep track of words

                        if(is_ip) begin
                           flow_entry[`OPENFLOW_ENTRY_IP_DST_POS + 15:`OPENFLOW_ENTRY_IP_DST_POS]
                            <= in_data[63:48];
                           is_ip    <= 0;
                           /* for Hash function */
                            dst_ip[15:0] <= in_data[63:48];
                        end

                        if(is_tcp_udp) begin
                           if(ip_hdr_len == 5) begin
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_SRC_POS + 15:`OPENFLOW_ENTRY_TRANSP_SRC_POS]    <= in_data[47:32];
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_DST_POS + 15:`OPENFLOW_ENTRY_TRANSP_DST_POS]    <= in_data[31:16];
                              /* for Hash function */
                              if(dst_port == HTTP)
                                counter <= 7;

                           end // if (ip_hdr_len == 5)
                           else if(ip_hdr_len == 6) begin
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_SRC_POS + 15:`OPENFLOW_ENTRY_TRANSP_SRC_POS]    <= in_data[15:0];
                           end
                           else if(ip_hdr_len == 4) begin
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_DST_POS + 15:`OPENFLOW_ENTRY_TRANSP_DST_POS]    <= in_data[63:48];
                           end // if (ip_hdr_len == 4)
                        end
                        else if (is_icmp) begin
                           if(ip_hdr_len == 5) begin
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_SRC_POS + 15:`OPENFLOW_ENTRY_TRANSP_SRC_POS + 8] <= 8'h0;
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_SRC_POS +  7:`OPENFLOW_ENTRY_TRANSP_SRC_POS]     <= in_data[47:40];
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_DST_POS + 15:`OPENFLOW_ENTRY_TRANSP_DST_POS + 8] <= 8'h0;
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_DST_POS +  7:`OPENFLOW_ENTRY_TRANSP_DST_POS]     <= in_data[39:32];
                           end // if (ip_hdr_len == 5)
                           else if(ip_hdr_len == 6) begin
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_SRC_POS + 15:`OPENFLOW_ENTRY_TRANSP_SRC_POS + 8] <= 8'h0;
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_SRC_POS +  7:`OPENFLOW_ENTRY_TRANSP_SRC_POS]     <= in_data[15:8];
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_DST_POS + 15:`OPENFLOW_ENTRY_TRANSP_DST_POS + 8] <= 8'h0;
                              flow_entry[`OPENFLOW_ENTRY_TRANSP_DST_POS +  7:`OPENFLOW_ENTRY_TRANSP_DST_POS]     <= in_data[7:0];
                           end // if (ip_hdr_len == 6).  if(ip_hder_len ==4), nothing to do.
                        end // if ((is_tcp_udp || is_icmp) && ip_hdr_len >= 4)
                        if(!(is_tcp_udp || is_icmp)
                           || ((is_tcp_udp || is_icmp)
                               && (ip_hdr_len == 5
                                   || ip_hdr_len == 4))) begin
                           flow_entry_vld    <= 1'b1;
                           /* check for eop */
                            /* check for eop IF not HTTPGET*/
                          if(dst_port!=HTTP) begin
                             if(in_ctrl != 0) begin
                                state    <= RESET_FLOW_ENTRY;
                             end
                             else begin
                                state    <= WAIT_EOP;
                             end
                          end
                        end // else: !if(is_tcp_udp || is_icmp)
                     end // case: IP_DST_LO_TRANSP_PORTS_WORD

                     ARP_DST_HI_WORD: begin
                        flow_entry[`OPENFLOW_ENTRY_IP_DST_POS + 31:`OPENFLOW_ENTRY_IP_DST_POS + 16]
                           <= in_data[15:0];
                     end

                     //default: begin
                     ARP_DST_LO_WORD: begin
                        flow_entry[`OPENFLOW_ENTRY_IP_DST_POS + 15:`OPENFLOW_ENTRY_IP_DST_POS]
                           <= in_data[63:48];
                        is_arp            <= 0;
                        flow_entry_vld    <= 1'b1;
                        /* check for eop */
                        if(in_ctrl != 0) begin
                           state    <= RESET_FLOW_ENTRY;
                        end
                        else begin
                           state    <= WAIT_EOP;
                        end
                     end // case: ARP_DST_LO_WORD

                     CHECK_TCP_LEN: begin                                // word 6 -- counter = 7
                       flow_entry_vld    <= 1'b0;

                       if (tcp_hdr_len == WIN_TCP_HDR_LEN) begin
                         win_pkt <= 1;
                       end
                       else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                       end
                     end

                     WORD_7: begin
                        if (win_pkt) begin
                          if (req_meth_win == GE) begin
                             is_get_pkt_win <= 1;
                          end
                        end
                        else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                        end
                     end

                     WORD_8: begin                              // word 8 -- counter = 9
                       if(is_get_pkt_win) begin
                          in_data_hash <= {in_data_hash[255:64],{16'b0,URL_win}};
                          if (is_sp_win_word8) begin
                            counter <= WORD_27;
                          end
                       end
                       else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                       end
                     end

                    WORD_9: begin                               // counter = 10
                        if(is_get_pkt_win) begin
                            in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};                          
                            if(is_sp)  begin
                              counter <= WORD_27;
                            end
                        end  
                        else if (req_meth_unix == GET) begin
                              is_get_pkt_unix <= 1;
                              //in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                              in_data_hash <= {in_data_hash[255:16],in_data[15:0]};
                              if(is_sp_linux_word9) begin
                                counter <= WORD_27;
                              end
                            end 
                        else begin
                              state <= WAIT_EOP;
                        end
                            
                        
                    end // end WORD_9

                    WORD_10: begin                                  // counter = 11
                      if(is_get_pkt_win || is_get_pkt_unix) begin
                        in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                        if(is_sp)  begin
                          counter <= WORD_27;
                          
                        end 
                      end
                      else 
                        state <= WAIT_EOP;
                    end // end WORD_10

                    WORD_11: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_11

                    WORD_12: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_12

                    WORD_13: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_13

                    WORD_14: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_14

                    WORD_15: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_15

                    WORD_16: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_16

                    WORD_17: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_17

                    WORD_18: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_18

                    WORD_19: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_19

                    WORD_20: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_20

                    WORD_21: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_21

                    WORD_22: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_22

                    WORD_23: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_23

                    WORD_24: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_24

                    WORD_25: begin
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                      if(is_sp) begin
                        counter <= WORD_27;
                        
                      end
                      else if(in_ctrl != 0) begin
                              state    <= RESET_FLOW_ENTRY;
                      end
                    end // end WORD_25

                    WORD_26: begin                     
                      counter <= WORD_27;
                      in_data_hash <= {in_data_hash[191:0],{in_data & mask_URI}};
                    end // end WORD_26

                    WORD_27: begin
                      // hash function
                      addr_hash    <= crc_func_0({src_ip, in_data_hash[255:32]}, dst_ip);
                      in_data_hash <= 0;
                      hash_vld     <= 1;
                      state <= WAIT_EOP;
                    end

                  endcase // case(counter)
               end // if (in_wr)
            end // case: PKT_WORDS

            WAIT_EOP: begin
               flow_entry_vld    <= 1'b0;
               //
               is_get_pkt_win     <= 0;
               is_get_pkt_unix    <= 0;
               win_pkt            <= 0;
               hash_vld <= 0;
               if(in_ctrl!=0 & in_wr) begin
                  state             <= MODULE_HDRS;
                  flow_entry        <= flow_entry_default;
                  pkt_size          <= 0;
               end
            end

         endcase // case(state)
      end // else: !if(reset)
   end // always @ (posedge clk)

endmodule // header_parser

