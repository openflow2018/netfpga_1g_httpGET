/* ****************************************************************************
 * vim:set shiftwidth=2 softtabstop=2 expandtab:
 * $Id: counterdump.c 5455 2009-05-05 18:18:16Z g9coving $
 *
 * Module:  counterdump.c
 * Project: NetFPGA OpenFlow Switch WFQ
 * Description: dumps the MAC Rx/Tx counters to stdout
 * Author: Jad Naous
 *
 * Modified by: Hai Tran
 * Added registers at WFQ_top_simple and header_parser
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <net/if.h>

//#include "../../lib/C/reg_defines_openflow_switch.h"
#include "../../lib/C/reg_defines_openflow_switch.h"
#include "../../../../lib/C/common/nf2.h"
#include "../../../../lib/C/common/nf2util.h"

#define PATHLEN   80

#define DEFAULT_IFACE "nf2c0"

/* Global vars */
static struct nf2device nf2;

/* Function declarations */
void dumpCounts();
void processArgs (int , char **);
void usage (void);
// void dumpSharedBuffer();
// void check_weight();
// void check_ftime();
void check_share_buffer();

void check_tag_sort();
void check_ftime_tag_25_02();
void check_DDOS1 ();
void check_DDOS2 ();
//void check_state_url_extract ();


int main(int argc, char *argv[])
{
  nf2.device_name = DEFAULT_IFACE;

  processArgs(argc, argv);

  // Open the interface if possible
  if (check_iface(&nf2))
    {
      exit(1);
    }
  if (openDescriptor(&nf2))
    {
      exit(1);
    }
  // while(1) {
  //   dumpCounts();

  //   // dump header parser
  //   // dumpHeaderParser();

  //   // dump WFQ
  //   // dumpWFQ();
  //   // check_weight();
  //   check_ftime();
  // }
   // dumpCounts();
  // check_ftime();
  // check_share_buffer();
    // check_tag_sort();
    // check_ftime_tag_25_02();

   //  while(1){
   //  check_DDOS1 ();
   //  check_DDOS2 ();
   // }
   // check_state_url_extract();


    test_1();
    check_DDOS1 ();
    check_DDOS2 ();




    closeDescriptor(&nf2);

  return 0;
}

void test_1(){
  unsigned temp1,temp2;
  unsigned val1,val2;
  readReg(&nf2, DDOS_EXTRACT_SRC_IP_REG, &val1);
  printf("src_IP: %04x\n", val1);
  readReg(&nf2, DDOS_EXTRACT_DST_IP_REG, &val2);
  printf("dst_IP: %04x\n", val2);
  temp1 = val1;
  temp2 = val2;

  while(1){
    readReg(&nf2, DDOS_EXTRACT_SRC_IP_REG, &val1);
    readReg(&nf2, DDOS_EXTRACT_DST_IP_REG, &val2);
    if(temp1 != val1){
       printf("src_IP: %04x\n", val1);
       temp1 = val1;
    }
    if(temp2 != val2){
       printf("src_IP: %04x\n", val2);
       temp2 = val2;
    }
  }

}


void dumpCounts()
{
  unsigned val;

  readReg(&nf2, MAC_GRP_0_RX_QUEUE_NUM_PKTS_STORED_REG, &val);
  printf("Num pkts received on port 0:           %u\n", val);
  readReg(&nf2, MAC_GRP_0_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG, &val);
  printf("Num pkts dropped (rx queue 0 full):    %u\n", val);
  readReg(&nf2, MAC_GRP_0_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG, &val);
  printf("Num pkts dropped (bad fcs q 0):        %u\n", val);
  readReg(&nf2, MAC_GRP_0_RX_QUEUE_NUM_BYTES_PUSHED_REG, &val);
  printf("Num bytes received on port 0:          %u\n", val);
  readReg(&nf2, MAC_GRP_0_TX_QUEUE_NUM_PKTS_SENT_REG, &val);
  printf("Num pkts sent from port 0:             %u\n", val);
  readReg(&nf2, MAC_GRP_0_TX_QUEUE_NUM_BYTES_PUSHED_REG, &val);
  printf("Num bytes sent from port 0:            %u\n\n", val);

  readReg(&nf2, MAC_GRP_1_RX_QUEUE_NUM_PKTS_STORED_REG, &val);
  printf("Num pkts received on port 1:           %u\n", val);
  readReg(&nf2, MAC_GRP_1_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG, &val);
  printf("Num pkts dropped (rx queue 1 full):    %u\n", val);
  readReg(&nf2, MAC_GRP_1_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG, &val);
  printf("Num pkts dropped (bad fcs q 1):        %u\n", val);
  readReg(&nf2, MAC_GRP_1_RX_QUEUE_NUM_BYTES_PUSHED_REG, &val);
  printf("Num bytes received on port 1:          %u\n", val);
  readReg(&nf2, MAC_GRP_1_TX_QUEUE_NUM_PKTS_SENT_REG, &val);
  printf("Num pkts sent from port 1:             %u\n", val);
  readReg(&nf2, MAC_GRP_1_TX_QUEUE_NUM_BYTES_PUSHED_REG, &val);
  printf("Num bytes sent from port 1:            %u\n\n", val);

  readReg(&nf2, MAC_GRP_2_RX_QUEUE_NUM_PKTS_STORED_REG, &val);
  printf("Num pkts received on port 2:           %u\n", val);
  readReg(&nf2, MAC_GRP_2_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG, &val);
  printf("Num pkts dropped (rx queue 2 full):    %u\n", val);
  readReg(&nf2, MAC_GRP_2_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG, &val);
  printf("Num pkts dropped (bad fcs q 2):        %u\n", val);
  readReg(&nf2, MAC_GRP_2_RX_QUEUE_NUM_BYTES_PUSHED_REG, &val);
  printf("Num bytes received on port 2:          %u\n", val);
  readReg(&nf2, MAC_GRP_2_TX_QUEUE_NUM_PKTS_SENT_REG, &val);
  printf("Num pkts sent from port 2:             %u\n", val);
  readReg(&nf2, MAC_GRP_2_TX_QUEUE_NUM_BYTES_PUSHED_REG, &val);
  printf("Num bytes sent from port 2:            %u\n\n", val);

  readReg(&nf2, MAC_GRP_3_RX_QUEUE_NUM_PKTS_STORED_REG, &val);
  printf("Num pkts received on port 3:           %u\n", val);
  readReg(&nf2, MAC_GRP_3_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG, &val);
  printf("Num pkts dropped (rx queue 3 full):    %u\n", val);
  readReg(&nf2, MAC_GRP_3_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG, &val);
  printf("Num pkts dropped (bad fcs q 3):        %u\n", val);
  readReg(&nf2, MAC_GRP_3_RX_QUEUE_NUM_BYTES_PUSHED_REG, &val);
  printf("Num bytes received on port 3:          %u\n", val);
  readReg(&nf2, MAC_GRP_3_TX_QUEUE_NUM_PKTS_SENT_REG, &val);
  printf("Num pkts sent from port 3:             %u\n", val);
  readReg(&nf2, MAC_GRP_3_TX_QUEUE_NUM_BYTES_PUSHED_REG, &val);
  printf("Num bytes sent from port 3:            %u\n\n", val);
}

// void dumpSharedBuffer()
// {
//   unsigned val;
//   readReg(&nf2, SHARED_BUFFER_ESRC_REG, &val);
//   printf("Thanh ghi trong khoi shared buffer:    %u\n", val);
// }

// void check_weight()
// {
//   unsigned val;
//   readReg(&nf2, OPENFLOW_LOOKUP_FIFO_WEIGHT_REG, &val);
//   printf("Cac tin hieu trong output_port_lookup, 9 so 0, wfq_flow_id, wfq_flow_weight, wfq_pkt_size: %u\n", val);
// }

// void check_ftime () 
// {
//   unsigned val;
//   readReg(&nf2, WFQ_COMPUTATION_ESRC_FTIME_REG, &val);
//   printf("Cac tin hieu trong wfq_computation 14 so 0, out_wr, odone, oftime: %u\n", val);
// }

// void check_share_buffer ()
// {
//   unsigned val;
//   readReg(&nf2, SHARE_BUFFER_ESRC_SHARE_BUFFER_REG, &val);
//   // printf("Cac tin hieu trong share_buffer la 7 so 0, rd_req, wr_req, sb_nearly_full, sb_empty, ip, ctrl: %u\n", val);
//   printf("Cac tin hieu trong share_buffer la 30 so 0, out_sb_empty, nearly_full: %u\n", val);
// }

// void check_tag_sort ()
// {
  
//   unsigned val;
//   readReg(&nf2, WFQ_TOP_SIMPLE_ESRC_WFQ_TAG_SORT_REG, &val);
//   printf("Cac tin hieu trong wfq_tag_simple la 7 so 0, out_ready, ts_oflow_id_min, ts_oflow_weight_min, ts_opk_addr_min: %u\n", val);
// }

// void check_ftime_tag_25_02 ()
// {
//   unsigned val;
//   readReg(&nf2, WFQ_TOP_SIMPLE_ESRC_WFQ_COMPUTATION_REG, &val);
//   printf("Cac tin hieu trong wfq_tag_simple la 16 so 0, wfq_ftag_out: %u\n", val);
// }

void check_DDOS1 (){
  unsigned val;
  readReg(&nf2, DDOS_DEFENDER_DDOS_0_REG, &val);
  // printf("Cac tin hieu trong share_buffer la 7 so 0, rd_req, wr_req, sb_nearly_full, sb_empty, ip, ctrl: %u\n", val);
  printf("A_state_url_extract: %04x\n", val);
}

void check_DDOS2 (){
  unsigned val;
  readReg(&nf2, DDOS_DEFENDER_DDOS_1_REG, &val);
  // printf("Cac tin hieu trong share_buffer la 7 so 0, rd_req, wr_req, sb_nearly_full, sb_empty, ip, ctrl: %u\n", val);
  printf("B_dst_ip_lo_check___word_IP_LEN_ID: %04x\n", val);
}


// void check_state_url_extract (){
//   unsigned val;
//   readReg(&nf2, URL_EXTRACT_STATE_REG, &val);
//   // printf("Cac tin hieu trong share_buffer la 7 so 0, rd_req, wr_req, sb_nearly_full, sb_empty, ip, ctrl: %u\n", val);
//   printf("STATE URL EXTRACT: %04x\n", val);
// }








/*
 *  Process the arguments.
 */
void processArgs (int argc, char **argv )
{
  char c;

  /* don't want getopt to moan - I can do that just fine thanks! */
  opterr = 0;

  while ((c = getopt (argc, argv, "i:h")) != -1)
    {
      switch (c)
  {
  case 'i': /* interface name */
    nf2.device_name = optarg;
    break;
  case '?':
    if (isprint (optopt))
      fprintf (stderr, "Unknown option `-%c'.\n", optopt);
    else
      fprintf (stderr,
         "Unknown option character `\\x%x'.\n",
         optopt);
  case 'h':
  default:
    usage();
    exit(1);
  }
    }
}


/*
 *  Describe usage of this program.
 */
void usage (void)
{
  printf("Usage: ./counterdump <options> \n\n");
  printf("Options: -i <iface> : interface name (default nf2c0)\n");
  printf("         -h : Print this message and exit.\n");
}
