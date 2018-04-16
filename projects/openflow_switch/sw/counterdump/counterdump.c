/* ****************************************************************************
 * vim:set shiftwidth=2 softtabstop=2 expandtab:
 * $Id: counterdump.c 5455 2009-05-05 18:18:16Z g9coving $
 *
 * Module:  counterdump.c
 * Project: NetFPGA OpenFlow Switch WFQ
 * Description: dumps the MAC Rx/Tx counters to stdout
 * Authors: Viet An - Phung Luan
 *
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <sys/socket.h>

#include <net/if.h>

#include <time.h>

#include "../../lib/C/reg_defines_openflow_switch.h"
#include "../../../../lib/C/common/nf2.h"
#include "../../../../lib/C/common/nf2util.h"

#define DEFAULT_IFACE "nf2c0"

/* Global vars */
static struct nf2device nf2;

/* Function declarations */
void usage (void);
void printIP(unsigned);
void test_2(void);

int main(int argc, char *argv[])
{
  nf2.device_name = DEFAULT_IFACE;
  // Open the interface if possible
  if (check_iface(&nf2)){
      exit(1);
    }
  if (openDescriptor(&nf2)){
      exit(1);
  }

    test_2();
  

  
  closeDescriptor(&nf2);
  return 0;
}


void test_2(void){
  
  unsigned src_ip1, src_ip1_temp;
  unsigned count1, count1_temp;
  unsigned detected_ip, detected_ip_temp;
  unsigned num_pkt_drop_6, num_pkt_drop_6_temp;
  unsigned num_pkt_drop_0, num_pkt_drop_0_temp;
  unsigned ctrl_mode;

//-- check writeReg
  unsigned exact_hits;

  unsigned mode = 111;
//-- write control mode:
  int i, j;
  int c = 0;
  writeReg(&nf2, OPENFLOW_LOOKUP_EXACT_HITS_REG, 789123);
  readReg(&nf2, OPENFLOW_LOOKUP_EXACT_HITS_REG, &exact_hits);
  printf("exact_hits: %d\n", exact_hits);



  writeReg(&nf2, TOP_DDOS_CONTROL_MODE_REG, mode);
  readReg(&nf2, TOP_DDOS_CONTROL_MODE_REG, &ctrl_mode);

  printf("CONTROL_MODE: %d\n", ctrl_mode);


//---
  readReg(&nf2, TOP_DDOS_SRC_IP_1_REG, &src_ip1);
  readReg(&nf2, TOP_DDOS_COUNT_1_REG, &count1);
  readReg(&nf2, TOP_DDOS_DETECTED_IP_REG, &detected_ip);
  readReg(&nf2, OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_6_REG, &num_pkt_drop_6);
  readReg(&nf2, OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_0_REG, &num_pkt_drop_0);

  src_ip1_temp = src_ip1;
  count1_temp = count1;
  detected_ip_temp = detected_ip;
  num_pkt_drop_6_temp = num_pkt_drop_6;
  num_pkt_drop_0_temp = num_pkt_drop_0;

  while(1){
    readReg(&nf2, TOP_DDOS_SRC_IP_1_REG, &src_ip1_temp);
    readReg(&nf2, TOP_DDOS_COUNT_1_REG, &count1_temp);
    readReg(&nf2, TOP_DDOS_DETECTED_IP_REG, &detected_ip_temp);
    readReg(&nf2, OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_6_REG, &num_pkt_drop_6_temp);
    readReg(&nf2, OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_0_REG, &num_pkt_drop_0_temp);

    if((src_ip1_temp != src_ip1)||(count1_temp != count1)
        ||(detected_ip_temp != detected_ip) 
        || (num_pkt_drop_6 != num_pkt_drop_6_temp) 
        || (num_pkt_drop_0 != num_pkt_drop_0_temp))
        // if(num_pkt_drop_0 != num_pkt_drop_0_temp)

    {
      printIP(src_ip1_temp); 
      printf("%04x\n", count1_temp);
      printIP(detected_ip_temp); 
      printf("OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_6_REG: %d\n", num_pkt_drop_6_temp);
      printf("OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_0_REG: %d\n", num_pkt_drop_0_temp);

      printf("CONTROL_MODE: %d\n", ctrl_mode);
      readReg(&nf2, OPENFLOW_LOOKUP_EXACT_HITS_REG, &exact_hits);
      printf("exact_hits: %d\n", exact_hits);

      printf("\n\n\n");
      src_ip1 = src_ip1_temp;
      count1 = count1_temp;
      detected_ip = detected_ip_temp;

      num_pkt_drop_6 = num_pkt_drop_6_temp;
      num_pkt_drop_0 = num_pkt_drop_0_temp;
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

void printIP(unsigned ip)
{
  printf("%u.%u.%u.%u \n",
      ((ip>>24)&0xff), ((ip>>16)&0xff), ((ip>>8)&0xff), ((ip>>0)&0xff)
    );

}