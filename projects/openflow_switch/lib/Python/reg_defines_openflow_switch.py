#!/usr/bin/python
#############################################################
#
# Python register defines
#
# Project: OpenFlow Switch (openflow_switch)
# Description: OpenFlow Switch
#
#############################################################

# -------------------------------------
#   Version Information
# -------------------------------------
def DEVICE_ID ():
    return 0

def DEVICE_MAJOR ():
    return 1

def DEVICE_MINOR ():
    return 0

def DEVICE_REVISION ():
    return 4

def DEVICE_PROJ_DIR ():
    return "openflow_switch"

def DEVICE_PROJ_NAME ():
    return "OpenFlow Switch"

def DEVICE_PROJ_DESC ():
    return "OpenFlow Switch"


# -------------------------------------
#   Constants
# -------------------------------------

# ===== File: lib/verilog/core/common/xml/global.xml =====

# Maximum number of phy ports
def MAX_PHY_PORTS ():                           
    return 4

# PCI address bus width
def PCI_ADDR_WIDTH ():                          
    return 32

# PCI data bus width
def PCI_DATA_WIDTH ():                          
    return 32

# PCI byte enable bus width
def PCI_BE_WIDTH ():                            
    return 4

# CPCI--CNET address bus width. This is byte addresses even though bottom bits are zero.
def CPCI_CNET_ADDR_WIDTH ():                    
    return 27

# CPCI--CNET data bus width
def CPCI_CNET_DATA_WIDTH ():                    
    return 32

# CPCI--Virtex address bus width. This is byte addresses even though bottom bits are zero.
def CPCI_NF2_ADDR_WIDTH ():                     
    return 27

# CPCI--Virtex data bus width
def CPCI_NF2_DATA_WIDTH ():                     
    return 32

# DMA data bus width
def DMA_DATA_WIDTH ():                          
    return 32

# DMA control bus width
def DMA_CTRL_WIDTH ():                          
    return 4

# CPCI debug bus width
def CPCI_DEBUG_DATA_WIDTH ():                   
    return 29

# SRAM address width
def SRAM_ADDR_WIDTH ():                         
    return 19

# SRAM data width
def SRAM_DATA_WIDTH ():                         
    return 36

# DRAM address width
def DRAM_ADDR_WIDTH ():                         
    return 24


# ===== File: lib/verilog/core/common/xml/nf_defines.xml =====

# Clock period of 125 MHz clock in ns
def FAST_CLK_PERIOD ():                         
    return 8

# Clock period of 62.5 MHz clock in ns
def SLOW_CLK_PERIOD ():                         
    return 16

# Header value used by the IO queues
def IO_QUEUE_STAGE_NUM ():                      
    return 0xff

# Data path data width
def DATA_WIDTH ():                              
    return 64

# Data path control width
def CTRL_WIDTH ():                              
    return 8


# ===== File: projects/openflow_switch/include/output_port_lookup.xml =====

def FAST_CLOCK_PERIOD ():                       
    return 8


# ===== File: projects/openflow_switch/include/vlan_remover.xml =====

def VLAN_CTRL_WORD ():                          
    return 0x42

def VLAN_ETHERTYPE ():                          
    return 0x8100


# ===== File: lib/verilog/core/output_queues/bram_output_queues/xml/bram_output_queues.xml =====

def NUM_OUTPUT_QUEUES ():                       
    return 8


# ===== File: projects/openflow_switch/include/opl_processor.xml =====

def NF2_OFPAT_OUTPUT ():                        
    return 0x0001

def NF2_OFPAT_SET_VLAN_VID ():                  
    return 0x0002

def NF2_OFPAT_SET_VLAN_PCP ():                  
    return 0x0004

def NF2_OFPAT_STRIP_VLAN ():                    
    return 0x0008

def NF2_OFPAT_SET_DL_SRC ():                    
    return 0x0010

def NF2_OFPAT_SET_DL_DST ():                    
    return 0x0020

def NF2_OFPAT_SET_NW_SRC ():                    
    return 0x0040

def NF2_OFPAT_SET_NW_DST ():                    
    return 0x0080

def NF2_OFPAT_SET_NW_TOS ():                    
    return 0x0100

def NF2_OFPAT_SET_TP_SRC ():                    
    return 0x0200

def NF2_OFPAT_SET_TP_DST ():                    
    return 0x0400


# ===== File: projects/openflow_switch/include/wildcard_match.xml =====

def OPENFLOW_WILDCARD_TABLE_SIZE ():            
    return 32

def OPENFLOW_WILDCARD_NUM_DATA_WORDS_USED ():   
    return 10

def OPENFLOW_WILDCARD_NUM_CMP_WORDS_USED ():    
    return 8


# ===== File: lib/verilog/core/utils/xml/device_id_reg.xml =====

# Total number of registers
def DEV_ID_NUM_REGS ():                         
    return 64

# Number of non string registers
def DEV_ID_NON_STR_REGS ():                     
    return 7

# Length of MD5 sum (bits)
def DEV_ID_MD5SUM_LENGTH ():                    
    return 128

# Project directory length (in words, not chars)
def DEV_ID_PROJ_DIR_WORD_LEN ():                
    return 16

# Project directory length (in bytes/chars)
def DEV_ID_PROJ_DIR_BYTE_LEN ():                
    return 64

# Project directory length (in bits)
def DEV_ID_PROJ_DIR_BIT_LEN ():                 
    return 512

# Project name length (in words, not chars)
def DEV_ID_PROJ_NAME_WORD_LEN ():               
    return 16

# Project name length (in bytes/chars)
def DEV_ID_PROJ_NAME_BYTE_LEN ():               
    return 64

# Project name length (in bits)
def DEV_ID_PROJ_NAME_BIT_LEN ():                
    return 512

# Device description length (in words, not chars)
def DEV_ID_PROJ_DESC_WORD_LEN ():               
    return 25

# Device description length (in bytes/chars)
def DEV_ID_PROJ_DESC_BYTE_LEN ():               
    return 100

# Device description length (in bits)
def DEV_ID_PROJ_DESC_BIT_LEN ():                
    return 800

# MD5 identifier (v1): MD5 sum of the string "device_id.v"
def DEV_ID_MD5_VALUE_V1_0 ():                   
    return 0x4071736d

def DEV_ID_MD5_VALUE_V1_1 ():                   
    return 0x8a603d2b

def DEV_ID_MD5_VALUE_V1_2 ():                   
    return 0x4d55f629

def DEV_ID_MD5_VALUE_V1_3 ():                   
    return 0x89a73c95


# MD5 identifier (v2): MD5 sum of the string "device_id.v:v2"
def DEV_ID_MD5_VALUE_V2_0 ():                   
    return 0x5e461ffe

def DEV_ID_MD5_VALUE_V2_1 ():                   
    return 0x439725c9

def DEV_ID_MD5_VALUE_V2_2 ():                   
    return 0x279a22a1

def DEV_ID_MD5_VALUE_V2_3 ():                   
    return 0x855f6c53


# Total number of registers (v1)
def DEV_ID_NUM_REGS_V1 ():                      
    return 64

# Number of non string registers (v1)
def DEV_ID_NON_STR_REGS_V1 ():                  
    return 7

# Project name length (v1: in words, not chars)
def DEV_ID_PROJ_NAME_WORD_LEN_V1 ():            
    return 25

# Project name length (v1: in bytes/chars)
def DEV_ID_PROJ_NAME_BYTE_LEN_V1 ():            
    return 100

# Project name length (v1: in bits)
def DEV_ID_PROJ_NAME_BIT_LEN_V1 ():             
    return 800


# ===== File: projects/openflow_switch/include/watchdog.xml =====

def WDT_CPCI_REG_CTRL ():                       
    return 0x00000008


# ===== File: projects/openflow_switch/include/header_parser.xml =====

def ETH_TYPE_IP ():                             
    return 0x0800

def ETH_TYPE_ARP ():                            
    return 0x0806

def IP_PROTO_TCP ():                            
    return 0x06

def IP_PROTO_UDP ():                            
    return 0x11

def IP_PROTO_ICMP ():                           
    return 0x01


# ===== File: lib/verilog/core/io_queues/cpu_dma_queue/xml/cpu_dma_queue.xml =====

def CPU_QUEUE_REGS_ENABLE ():                   
    return 0x00000000

def CPU_QUEUE_REGS_DISABLE ():                  
    return 0x00000001


# ===== File: lib/verilog/core/io_queues/ethernet_queue/xml/ethernet_mac.xml =====

# TX queue disable bit
def MAC_GRP_TX_QUEUE_DISABLE_BIT_NUM ():        
    return 0

# RX queue disable bit
def MAC_GRP_RX_QUEUE_DISABLE_BIT_NUM ():        
    return 1

# Reset MAC bit
def MAC_GRP_RESET_MAC_BIT_NUM ():               
    return 2

# MAC TX queue disable bit
def MAC_GRP_MAC_DISABLE_TX_BIT_NUM ():          
    return 3

# MAC RX queue disable bit
def MAC_GRP_MAC_DISABLE_RX_BIT_NUM ():          
    return 4

# MAC disable jumbo TX bit
def MAC_GRP_MAC_DIS_JUMBO_TX_BIT_NUM ():        
    return 5

# MAC disable jumbo RX bit
def MAC_GRP_MAC_DIS_JUMBO_RX_BIT_NUM ():        
    return 6

# MAC disable crc check disable bit
def MAC_GRP_MAC_DIS_CRC_CHECK_BIT_NUM ():       
    return 7

# MAC disable crc generate bit
def MAC_GRP_MAC_DIS_CRC_GEN_BIT_NUM ():         
    return 8


# ===== File: projects/openflow_switch/include/match_arbiter.xml =====

def OPENFLOW_ENTRY_TRANSP_DST_WIDTH ():         
    return 16

def OPENFLOW_ENTRY_TRANSP_DST_POS ():           
    return 0

def OPENFLOW_ENTRY_TRANSP_SRC_WIDTH ():         
    return 16

def OPENFLOW_ENTRY_TRANSP_SRC_POS ():           
    return 16

def OPENFLOW_ENTRY_IP_PROTO_WIDTH ():           
    return 8

def OPENFLOW_ENTRY_IP_PROTO_POS ():             
    return 32

def OPENFLOW_ENTRY_IP_DST_WIDTH ():             
    return 32

def OPENFLOW_ENTRY_IP_DST_POS ():               
    return 40

def OPENFLOW_ENTRY_IP_SRC_WIDTH ():             
    return 32

def OPENFLOW_ENTRY_IP_SRC_POS ():               
    return 72

def OPENFLOW_ENTRY_ETH_TYPE_WIDTH ():           
    return 16

def OPENFLOW_ENTRY_ETH_TYPE_POS ():             
    return 104

def OPENFLOW_ENTRY_ETH_DST_WIDTH ():            
    return 48

def OPENFLOW_ENTRY_ETH_DST_POS ():              
    return 120

def OPENFLOW_ENTRY_ETH_SRC_WIDTH ():            
    return 48

def OPENFLOW_ENTRY_ETH_SRC_POS ():              
    return 168

def OPENFLOW_ENTRY_SRC_PORT_WIDTH ():           
    return 8

def OPENFLOW_ENTRY_SRC_PORT_POS ():             
    return 216

def OPENFLOW_ENTRY_IP_TOS_WIDTH ():             
    return 8

def OPENFLOW_ENTRY_IP_TOS_POS ():               
    return 224

def OPENFLOW_ENTRY_VLAN_ID_WIDTH ():            
    return 16

def OPENFLOW_ENTRY_VLAN_ID_POS ():              
    return 232

def OPENFLOW_ENTRY_WIDTH ():                    
    return 248

# The actionfield is composed of a bitmask specifying actions to take and arguments.
def OPENFLOW_ACTION_WIDTH ():                   
    return 320

# Ports to forward on
def OPENFLOW_FORWARD_BITMASK_WIDTH ():          
    return 16

def OPENFLOW_FORWARD_BITMASK_POS ():            
    return 0

def OPENFLOW_NF2_ACTION_FLAG_WIDTH ():          
    return 16

def OPENFLOW_NF2_ACTION_FLAG_POS ():            
    return 16

# Vlan ID to be replaced
def OPENFLOW_SET_VLAN_VID_WIDTH ():             
    return 16

def OPENFLOW_SET_VLAN_VID_POS ():               
    return 32

# Vlan priority to be replaced
def OPENFLOW_SET_VLAN_PCP_WIDTH ():             
    return 8

def OPENFLOW_SET_VLAN_PCP_POS ():               
    return 48

# Source MAC address to be replaced
def OPENFLOW_SET_DL_SRC_WIDTH ():               
    return 48

def OPENFLOW_SET_DL_SRC_POS ():                 
    return 56

# Destination MAC address to be replaced
def OPENFLOW_SET_DL_DST_WIDTH ():               
    return 48

def OPENFLOW_SET_DL_DST_POS ():                 
    return 104

# Source network address to be replaced
def OPENFLOW_SET_NW_SRC_WIDTH ():               
    return 32

def OPENFLOW_SET_NW_SRC_POS ():                 
    return 152

# Destination network address to be replaced
def OPENFLOW_SET_NW_DST_WIDTH ():               
    return 32

def OPENFLOW_SET_NW_DST_POS ():                 
    return 184

# TOS to be replaced
def OPENFLOW_SET_NW_TOS_WIDTH ():               
    return 8

def OPENFLOW_SET_NW_TOS_POS ():                 
    return 216

# Source transport port to be replaced
def OPENFLOW_SET_TP_SRC_WIDTH ():               
    return 16

def OPENFLOW_SET_TP_SRC_POS ():                 
    return 224

# Destination transport port to be replaced
def OPENFLOW_SET_TP_DST_WIDTH ():               
    return 16

def OPENFLOW_SET_TP_DST_POS ():                 
    return 240


# ===== File: projects/openflow_switch/include/exact_match.xml =====

def OPENFLOW_EXACT_ENTRY_PKT_COUNTER_WIDTH ():  
    return 25

def OPENFLOW_EXACT_ENTRY_PKT_COUNTER_POS ():    
    return 0

def OPENFLOW_EXACT_ENTRY_LAST_SEEN_WIDTH ():    
    return 7

def OPENFLOW_EXACT_ENTRY_LAST_SEEN_POS ():      
    return 25

def OPENFLOW_EXACT_ENTRY_BYTE_COUNTER_WIDTH (): 
    return 32

def OPENFLOW_EXACT_ENTRY_BYTE_COUNTER_POS ():   
    return 32

def OPENFLOW_EXACT_ENTRY_HDR_BASE_POS ():       
    return 0x00000000

def OPENFLOW_EXACT_ENTRY_COUNTERS_POS ():       
    return 0x00000008

def OPENFLOW_EXACT_ENTRY_ACTION_BASE_POS ():    
    return 0x0000000a



## -------------------------------------
##   Modules
## -------------------------------------

# Module tags
def CORE_BASE_ADDR ():                     
    return 0x0000000

def DEV_ID_BASE_ADDR ():                   
    return 0x0400000

def MDIO_BASE_ADDR ():                     
    return 0x0440000

def DMA_BASE_ADDR ():                      
    return 0x0500000

def MAC_GRP_0_BASE_ADDR ():                
    return 0x0600000

def MAC_GRP_1_BASE_ADDR ():                
    return 0x0640000

def MAC_GRP_2_BASE_ADDR ():                
    return 0x0680000

def MAC_GRP_3_BASE_ADDR ():                
    return 0x06c0000

def CPU_QUEUE_0_BASE_ADDR ():              
    return 0x0700000

def CPU_QUEUE_1_BASE_ADDR ():              
    return 0x0740000

def CPU_QUEUE_2_BASE_ADDR ():              
    return 0x0780000

def CPU_QUEUE_3_BASE_ADDR ():              
    return 0x07c0000

def SRAM_BASE_ADDR ():                     
    return 0x1000000

def UDP_BASE_ADDR ():                      
    return 0x2000000

def OPENFLOW_LOOKUP_BASE_ADDR ():          
    return 0x2000000

def IN_ARB_BASE_ADDR ():                   
    return 0x2000100

def VLAN_REMOVER_BASE_ADDR ():             
    return 0x2000200

def OPL_PROCESSOR_BASE_ADDR ():            
    return 0x2000240

def HEADER_PARSER_BASE_ADDR ():            
    return 0x2000280

def TOP_DDOS_BASE_ADDR ():                 
    return 0x20002c0

def BRAM_OQ_BASE_ADDR ():                  
    return 0x2000300

def WDT_BASE_ADDR ():                      
    return 0x2000400

def MATCH_ARBITER_BASE_ADDR ():            
    return 0x2000500

def EXACT_MATCH_BASE_ADDR ():              
    return 0x2000540

def OPENFLOW_WILDCARD_LOOKUP_BASE_ADDR (): 
    return 0x2001000

def DRAM_BASE_ADDR ():                     
    return 0x4000000


def CPU_QUEUE_OFFSET ():                
    return 0x0040000

def MAC_GRP_OFFSET ():                  
    return 0x0040000



# -------------------------------------
#   Registers
# -------------------------------------

# Name: device_id (DEV_ID)
# Description: Device identification
# File: lib/verilog/core/utils/xml/device_id_reg.xml
def DEV_ID_MD5_0_REG ():        
    return 0x0400000

def DEV_ID_MD5_1_REG ():        
    return 0x0400004

def DEV_ID_MD5_2_REG ():        
    return 0x0400008

def DEV_ID_MD5_3_REG ():        
    return 0x040000c

def DEV_ID_DEVICE_ID_REG ():    
    return 0x0400010

def DEV_ID_VERSION_REG ():      
    return 0x0400014

def DEV_ID_CPCI_ID_REG ():      
    return 0x0400018

def DEV_ID_PROJ_DIR_0_REG ():   
    return 0x040001c

def DEV_ID_PROJ_DIR_1_REG ():   
    return 0x0400020

def DEV_ID_PROJ_DIR_2_REG ():   
    return 0x0400024

def DEV_ID_PROJ_DIR_3_REG ():   
    return 0x0400028

def DEV_ID_PROJ_DIR_4_REG ():   
    return 0x040002c

def DEV_ID_PROJ_DIR_5_REG ():   
    return 0x0400030

def DEV_ID_PROJ_DIR_6_REG ():   
    return 0x0400034

def DEV_ID_PROJ_DIR_7_REG ():   
    return 0x0400038

def DEV_ID_PROJ_DIR_8_REG ():   
    return 0x040003c

def DEV_ID_PROJ_DIR_9_REG ():   
    return 0x0400040

def DEV_ID_PROJ_DIR_10_REG ():  
    return 0x0400044

def DEV_ID_PROJ_DIR_11_REG ():  
    return 0x0400048

def DEV_ID_PROJ_DIR_12_REG ():  
    return 0x040004c

def DEV_ID_PROJ_DIR_13_REG ():  
    return 0x0400050

def DEV_ID_PROJ_DIR_14_REG ():  
    return 0x0400054

def DEV_ID_PROJ_DIR_15_REG ():  
    return 0x0400058

def DEV_ID_PROJ_NAME_0_REG ():  
    return 0x040005c

def DEV_ID_PROJ_NAME_1_REG ():  
    return 0x0400060

def DEV_ID_PROJ_NAME_2_REG ():  
    return 0x0400064

def DEV_ID_PROJ_NAME_3_REG ():  
    return 0x0400068

def DEV_ID_PROJ_NAME_4_REG ():  
    return 0x040006c

def DEV_ID_PROJ_NAME_5_REG ():  
    return 0x0400070

def DEV_ID_PROJ_NAME_6_REG ():  
    return 0x0400074

def DEV_ID_PROJ_NAME_7_REG ():  
    return 0x0400078

def DEV_ID_PROJ_NAME_8_REG ():  
    return 0x040007c

def DEV_ID_PROJ_NAME_9_REG ():  
    return 0x0400080

def DEV_ID_PROJ_NAME_10_REG (): 
    return 0x0400084

def DEV_ID_PROJ_NAME_11_REG (): 
    return 0x0400088

def DEV_ID_PROJ_NAME_12_REG (): 
    return 0x040008c

def DEV_ID_PROJ_NAME_13_REG (): 
    return 0x0400090

def DEV_ID_PROJ_NAME_14_REG (): 
    return 0x0400094

def DEV_ID_PROJ_NAME_15_REG (): 
    return 0x0400098

def DEV_ID_PROJ_DESC_0_REG ():  
    return 0x040009c

def DEV_ID_PROJ_DESC_1_REG ():  
    return 0x04000a0

def DEV_ID_PROJ_DESC_2_REG ():  
    return 0x04000a4

def DEV_ID_PROJ_DESC_3_REG ():  
    return 0x04000a8

def DEV_ID_PROJ_DESC_4_REG ():  
    return 0x04000ac

def DEV_ID_PROJ_DESC_5_REG ():  
    return 0x04000b0

def DEV_ID_PROJ_DESC_6_REG ():  
    return 0x04000b4

def DEV_ID_PROJ_DESC_7_REG ():  
    return 0x04000b8

def DEV_ID_PROJ_DESC_8_REG ():  
    return 0x04000bc

def DEV_ID_PROJ_DESC_9_REG ():  
    return 0x04000c0

def DEV_ID_PROJ_DESC_10_REG (): 
    return 0x04000c4

def DEV_ID_PROJ_DESC_11_REG (): 
    return 0x04000c8

def DEV_ID_PROJ_DESC_12_REG (): 
    return 0x04000cc

def DEV_ID_PROJ_DESC_13_REG (): 
    return 0x04000d0

def DEV_ID_PROJ_DESC_14_REG (): 
    return 0x04000d4

def DEV_ID_PROJ_DESC_15_REG (): 
    return 0x04000d8

def DEV_ID_PROJ_DESC_16_REG (): 
    return 0x04000dc

def DEV_ID_PROJ_DESC_17_REG (): 
    return 0x04000e0

def DEV_ID_PROJ_DESC_18_REG (): 
    return 0x04000e4

def DEV_ID_PROJ_DESC_19_REG (): 
    return 0x04000e8

def DEV_ID_PROJ_DESC_20_REG (): 
    return 0x04000ec

def DEV_ID_PROJ_DESC_21_REG (): 
    return 0x04000f0

def DEV_ID_PROJ_DESC_22_REG (): 
    return 0x04000f4

def DEV_ID_PROJ_DESC_23_REG (): 
    return 0x04000f8

def DEV_ID_PROJ_DESC_24_REG (): 
    return 0x04000fc


# Name: mdio (MDIO)
# Description: MDIO interface
# File: lib/verilog/core/io/mdio/xml/mdio.xml
def MDIO_PHY_0_CONTROL_REG ():                                
    return 0x0440000

def MDIO_PHY_0_STATUS_REG ():                                 
    return 0x0440004

def MDIO_PHY_0_PHY_ID_HI_REG ():                              
    return 0x0440008

def MDIO_PHY_0_PHY_ID_LO_REG ():                              
    return 0x044000c

def MDIO_PHY_0_AUTONEGOTIATION_ADVERT_REG ():                 
    return 0x0440010

def MDIO_PHY_0_AUTONEG_LINK_PARTNER_BASE_PAGE_ABILITY_REG (): 
    return 0x0440014

def MDIO_PHY_0_AUTONEG_EXPANSION_REG ():                      
    return 0x0440018

def MDIO_PHY_0_AUTONEG_NEXT_PAGE_TX_REG ():                   
    return 0x044001c

def MDIO_PHY_0_AUTONEG_LINK_PARTNER_RCVD_NEXT_PAGE_REG ():    
    return 0x0440020

def MDIO_PHY_0_MASTER_SLAVE_CTRL_REG ():                      
    return 0x0440024

def MDIO_PHY_0_MASTER_SLAVE_STATUS_REG ():                    
    return 0x0440028

def MDIO_PHY_0_PSE_CTRL_REG ():                               
    return 0x044002c

def MDIO_PHY_0_PSE_STATUS_REG ():                             
    return 0x0440030

def MDIO_PHY_0_MMD_ACCESS_CTRL_REG ():                        
    return 0x0440034

def MDIO_PHY_0_MMD_ACCESS_STATUS_REG ():                      
    return 0x0440038

def MDIO_PHY_0_EXTENDED_STATUS_REG ():                        
    return 0x044003c

def MDIO_PHY_0_PHY_EXTENDED_CTRL_REG ():                      
    return 0x0440040

def MDIO_PHY_0_PHY_EXTENDED_STATUS_REG ():                    
    return 0x0440044

def MDIO_PHY_0_RX_ERROR_COUNT_REG ():                         
    return 0x0440048

def MDIO_PHY_0_FALSE_CARRIER_SENSE_COUNT_REG ():              
    return 0x044004c

def MDIO_PHY_0_RX_NOT_OK_COUNT_REG ():                        
    return 0x0440050

def MDIO_PHY_0_EXPANSION_1_REG ():                            
    return 0x0440054

def MDIO_PHY_0_EXPANSION_2_REG ():                            
    return 0x0440058

def MDIO_PHY_0_EXPANSION_REG_ACCESS_REG ():                   
    return 0x044005c

def MDIO_PHY_0_SHADOW_18_REG ():                              
    return 0x0440060

def MDIO_PHY_0_AUX_STATUS_REG ():                             
    return 0x0440064

def MDIO_PHY_0_INT_STATUS_REG ():                             
    return 0x0440068

def MDIO_PHY_0_INT_MASK_REG ():                               
    return 0x044006c

def MDIO_PHY_0_SHADOW_1C_REG ():                              
    return 0x0440070

def MDIO_PHY_0_SHADOW_1D_REG ():                              
    return 0x0440074

def MDIO_PHY_0_TEST_REG ():                                   
    return 0x0440078

def MDIO_PHY_0_RESERVED_REG ():                               
    return 0x044007c

def MDIO_PHY_1_CONTROL_REG ():                                
    return 0x0440080

def MDIO_PHY_1_STATUS_REG ():                                 
    return 0x0440084

def MDIO_PHY_1_PHY_ID_HI_REG ():                              
    return 0x0440088

def MDIO_PHY_1_PHY_ID_LO_REG ():                              
    return 0x044008c

def MDIO_PHY_1_AUTONEGOTIATION_ADVERT_REG ():                 
    return 0x0440090

def MDIO_PHY_1_AUTONEG_LINK_PARTNER_BASE_PAGE_ABILITY_REG (): 
    return 0x0440094

def MDIO_PHY_1_AUTONEG_EXPANSION_REG ():                      
    return 0x0440098

def MDIO_PHY_1_AUTONEG_NEXT_PAGE_TX_REG ():                   
    return 0x044009c

def MDIO_PHY_1_AUTONEG_LINK_PARTNER_RCVD_NEXT_PAGE_REG ():    
    return 0x04400a0

def MDIO_PHY_1_MASTER_SLAVE_CTRL_REG ():                      
    return 0x04400a4

def MDIO_PHY_1_MASTER_SLAVE_STATUS_REG ():                    
    return 0x04400a8

def MDIO_PHY_1_PSE_CTRL_REG ():                               
    return 0x04400ac

def MDIO_PHY_1_PSE_STATUS_REG ():                             
    return 0x04400b0

def MDIO_PHY_1_MMD_ACCESS_CTRL_REG ():                        
    return 0x04400b4

def MDIO_PHY_1_MMD_ACCESS_STATUS_REG ():                      
    return 0x04400b8

def MDIO_PHY_1_EXTENDED_STATUS_REG ():                        
    return 0x04400bc

def MDIO_PHY_1_PHY_EXTENDED_CTRL_REG ():                      
    return 0x04400c0

def MDIO_PHY_1_PHY_EXTENDED_STATUS_REG ():                    
    return 0x04400c4

def MDIO_PHY_1_RX_ERROR_COUNT_REG ():                         
    return 0x04400c8

def MDIO_PHY_1_FALSE_CARRIER_SENSE_COUNT_REG ():              
    return 0x04400cc

def MDIO_PHY_1_RX_NOT_OK_COUNT_REG ():                        
    return 0x04400d0

def MDIO_PHY_1_EXPANSION_1_REG ():                            
    return 0x04400d4

def MDIO_PHY_1_EXPANSION_2_REG ():                            
    return 0x04400d8

def MDIO_PHY_1_EXPANSION_REG_ACCESS_REG ():                   
    return 0x04400dc

def MDIO_PHY_1_SHADOW_18_REG ():                              
    return 0x04400e0

def MDIO_PHY_1_AUX_STATUS_REG ():                             
    return 0x04400e4

def MDIO_PHY_1_INT_STATUS_REG ():                             
    return 0x04400e8

def MDIO_PHY_1_INT_MASK_REG ():                               
    return 0x04400ec

def MDIO_PHY_1_SHADOW_1C_REG ():                              
    return 0x04400f0

def MDIO_PHY_1_SHADOW_1D_REG ():                              
    return 0x04400f4

def MDIO_PHY_1_TEST_REG ():                                   
    return 0x04400f8

def MDIO_PHY_1_RESERVED_REG ():                               
    return 0x04400fc

def MDIO_PHY_2_CONTROL_REG ():                                
    return 0x0440100

def MDIO_PHY_2_STATUS_REG ():                                 
    return 0x0440104

def MDIO_PHY_2_PHY_ID_HI_REG ():                              
    return 0x0440108

def MDIO_PHY_2_PHY_ID_LO_REG ():                              
    return 0x044010c

def MDIO_PHY_2_AUTONEGOTIATION_ADVERT_REG ():                 
    return 0x0440110

def MDIO_PHY_2_AUTONEG_LINK_PARTNER_BASE_PAGE_ABILITY_REG (): 
    return 0x0440114

def MDIO_PHY_2_AUTONEG_EXPANSION_REG ():                      
    return 0x0440118

def MDIO_PHY_2_AUTONEG_NEXT_PAGE_TX_REG ():                   
    return 0x044011c

def MDIO_PHY_2_AUTONEG_LINK_PARTNER_RCVD_NEXT_PAGE_REG ():    
    return 0x0440120

def MDIO_PHY_2_MASTER_SLAVE_CTRL_REG ():                      
    return 0x0440124

def MDIO_PHY_2_MASTER_SLAVE_STATUS_REG ():                    
    return 0x0440128

def MDIO_PHY_2_PSE_CTRL_REG ():                               
    return 0x044012c

def MDIO_PHY_2_PSE_STATUS_REG ():                             
    return 0x0440130

def MDIO_PHY_2_MMD_ACCESS_CTRL_REG ():                        
    return 0x0440134

def MDIO_PHY_2_MMD_ACCESS_STATUS_REG ():                      
    return 0x0440138

def MDIO_PHY_2_EXTENDED_STATUS_REG ():                        
    return 0x044013c

def MDIO_PHY_2_PHY_EXTENDED_CTRL_REG ():                      
    return 0x0440140

def MDIO_PHY_2_PHY_EXTENDED_STATUS_REG ():                    
    return 0x0440144

def MDIO_PHY_2_RX_ERROR_COUNT_REG ():                         
    return 0x0440148

def MDIO_PHY_2_FALSE_CARRIER_SENSE_COUNT_REG ():              
    return 0x044014c

def MDIO_PHY_2_RX_NOT_OK_COUNT_REG ():                        
    return 0x0440150

def MDIO_PHY_2_EXPANSION_1_REG ():                            
    return 0x0440154

def MDIO_PHY_2_EXPANSION_2_REG ():                            
    return 0x0440158

def MDIO_PHY_2_EXPANSION_REG_ACCESS_REG ():                   
    return 0x044015c

def MDIO_PHY_2_SHADOW_18_REG ():                              
    return 0x0440160

def MDIO_PHY_2_AUX_STATUS_REG ():                             
    return 0x0440164

def MDIO_PHY_2_INT_STATUS_REG ():                             
    return 0x0440168

def MDIO_PHY_2_INT_MASK_REG ():                               
    return 0x044016c

def MDIO_PHY_2_SHADOW_1C_REG ():                              
    return 0x0440170

def MDIO_PHY_2_SHADOW_1D_REG ():                              
    return 0x0440174

def MDIO_PHY_2_TEST_REG ():                                   
    return 0x0440178

def MDIO_PHY_2_RESERVED_REG ():                               
    return 0x044017c

def MDIO_PHY_3_CONTROL_REG ():                                
    return 0x0440180

def MDIO_PHY_3_STATUS_REG ():                                 
    return 0x0440184

def MDIO_PHY_3_PHY_ID_HI_REG ():                              
    return 0x0440188

def MDIO_PHY_3_PHY_ID_LO_REG ():                              
    return 0x044018c

def MDIO_PHY_3_AUTONEGOTIATION_ADVERT_REG ():                 
    return 0x0440190

def MDIO_PHY_3_AUTONEG_LINK_PARTNER_BASE_PAGE_ABILITY_REG (): 
    return 0x0440194

def MDIO_PHY_3_AUTONEG_EXPANSION_REG ():                      
    return 0x0440198

def MDIO_PHY_3_AUTONEG_NEXT_PAGE_TX_REG ():                   
    return 0x044019c

def MDIO_PHY_3_AUTONEG_LINK_PARTNER_RCVD_NEXT_PAGE_REG ():    
    return 0x04401a0

def MDIO_PHY_3_MASTER_SLAVE_CTRL_REG ():                      
    return 0x04401a4

def MDIO_PHY_3_MASTER_SLAVE_STATUS_REG ():                    
    return 0x04401a8

def MDIO_PHY_3_PSE_CTRL_REG ():                               
    return 0x04401ac

def MDIO_PHY_3_PSE_STATUS_REG ():                             
    return 0x04401b0

def MDIO_PHY_3_MMD_ACCESS_CTRL_REG ():                        
    return 0x04401b4

def MDIO_PHY_3_MMD_ACCESS_STATUS_REG ():                      
    return 0x04401b8

def MDIO_PHY_3_EXTENDED_STATUS_REG ():                        
    return 0x04401bc

def MDIO_PHY_3_PHY_EXTENDED_CTRL_REG ():                      
    return 0x04401c0

def MDIO_PHY_3_PHY_EXTENDED_STATUS_REG ():                    
    return 0x04401c4

def MDIO_PHY_3_RX_ERROR_COUNT_REG ():                         
    return 0x04401c8

def MDIO_PHY_3_FALSE_CARRIER_SENSE_COUNT_REG ():              
    return 0x04401cc

def MDIO_PHY_3_RX_NOT_OK_COUNT_REG ():                        
    return 0x04401d0

def MDIO_PHY_3_EXPANSION_1_REG ():                            
    return 0x04401d4

def MDIO_PHY_3_EXPANSION_2_REG ():                            
    return 0x04401d8

def MDIO_PHY_3_EXPANSION_REG_ACCESS_REG ():                   
    return 0x04401dc

def MDIO_PHY_3_SHADOW_18_REG ():                              
    return 0x04401e0

def MDIO_PHY_3_AUX_STATUS_REG ():                             
    return 0x04401e4

def MDIO_PHY_3_INT_STATUS_REG ():                             
    return 0x04401e8

def MDIO_PHY_3_INT_MASK_REG ():                               
    return 0x04401ec

def MDIO_PHY_3_SHADOW_1C_REG ():                              
    return 0x04401f0

def MDIO_PHY_3_SHADOW_1D_REG ():                              
    return 0x04401f4

def MDIO_PHY_3_TEST_REG ():                                   
    return 0x04401f8

def MDIO_PHY_3_RESERVED_REG ():                               
    return 0x04401fc


def MDIO_PHY_GROUP_BASE_ADDR ():
    return 0x0440000

def MDIO_PHY_GROUP_INST_OFFSET():
    return 0x0000080

# Name: dma (DMA)
# Description: DMA transfer module
# File: lib/verilog/core/dma/xml/dma.xml
def DMA_CTRL_REG ():              
    return 0x0500000

def DMA_NUM_INGRESS_PKTS_REG ():  
    return 0x0500004

def DMA_NUM_INGRESS_BYTES_REG (): 
    return 0x0500008

def DMA_NUM_EGRESS_PKTS_REG ():   
    return 0x050000c

def DMA_NUM_EGRESS_BYTES_REG ():  
    return 0x0500010

def DMA_NUM_TIMEOUTS_REG ():      
    return 0x0500014


# Name: nf2_mac_grp (MAC_GRP_0)
# Description: Ethernet MAC group
# File: lib/verilog/core/io_queues/ethernet_queue/xml/ethernet_mac.xml
def MAC_GRP_0_CONTROL_REG ():                        
    return 0x0600000

def MAC_GRP_0_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():     
    return 0x0600004

def MAC_GRP_0_RX_QUEUE_NUM_PKTS_STORED_REG ():       
    return 0x0600008

def MAC_GRP_0_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG (): 
    return 0x060000c

def MAC_GRP_0_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG ():  
    return 0x0600010

def MAC_GRP_0_RX_QUEUE_NUM_PKTS_DEQUEUED_REG ():     
    return 0x0600014

def MAC_GRP_0_RX_QUEUE_NUM_WORDS_PUSHED_REG ():      
    return 0x0600018

def MAC_GRP_0_RX_QUEUE_NUM_BYTES_PUSHED_REG ():      
    return 0x060001c

def MAC_GRP_0_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():     
    return 0x0600020

def MAC_GRP_0_TX_QUEUE_NUM_PKTS_ENQUEUED_REG ():     
    return 0x0600024

def MAC_GRP_0_TX_QUEUE_NUM_PKTS_SENT_REG ():         
    return 0x0600028

def MAC_GRP_0_TX_QUEUE_NUM_WORDS_PUSHED_REG ():      
    return 0x060002c

def MAC_GRP_0_TX_QUEUE_NUM_BYTES_PUSHED_REG ():      
    return 0x0600030


# Name: nf2_mac_grp (MAC_GRP_1)
# Description: Ethernet MAC group
# File: lib/verilog/core/io_queues/ethernet_queue/xml/ethernet_mac.xml
def MAC_GRP_1_CONTROL_REG ():                        
    return 0x0640000

def MAC_GRP_1_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():     
    return 0x0640004

def MAC_GRP_1_RX_QUEUE_NUM_PKTS_STORED_REG ():       
    return 0x0640008

def MAC_GRP_1_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG (): 
    return 0x064000c

def MAC_GRP_1_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG ():  
    return 0x0640010

def MAC_GRP_1_RX_QUEUE_NUM_PKTS_DEQUEUED_REG ():     
    return 0x0640014

def MAC_GRP_1_RX_QUEUE_NUM_WORDS_PUSHED_REG ():      
    return 0x0640018

def MAC_GRP_1_RX_QUEUE_NUM_BYTES_PUSHED_REG ():      
    return 0x064001c

def MAC_GRP_1_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():     
    return 0x0640020

def MAC_GRP_1_TX_QUEUE_NUM_PKTS_ENQUEUED_REG ():     
    return 0x0640024

def MAC_GRP_1_TX_QUEUE_NUM_PKTS_SENT_REG ():         
    return 0x0640028

def MAC_GRP_1_TX_QUEUE_NUM_WORDS_PUSHED_REG ():      
    return 0x064002c

def MAC_GRP_1_TX_QUEUE_NUM_BYTES_PUSHED_REG ():      
    return 0x0640030


# Name: nf2_mac_grp (MAC_GRP_2)
# Description: Ethernet MAC group
# File: lib/verilog/core/io_queues/ethernet_queue/xml/ethernet_mac.xml
def MAC_GRP_2_CONTROL_REG ():                        
    return 0x0680000

def MAC_GRP_2_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():     
    return 0x0680004

def MAC_GRP_2_RX_QUEUE_NUM_PKTS_STORED_REG ():       
    return 0x0680008

def MAC_GRP_2_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG (): 
    return 0x068000c

def MAC_GRP_2_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG ():  
    return 0x0680010

def MAC_GRP_2_RX_QUEUE_NUM_PKTS_DEQUEUED_REG ():     
    return 0x0680014

def MAC_GRP_2_RX_QUEUE_NUM_WORDS_PUSHED_REG ():      
    return 0x0680018

def MAC_GRP_2_RX_QUEUE_NUM_BYTES_PUSHED_REG ():      
    return 0x068001c

def MAC_GRP_2_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():     
    return 0x0680020

def MAC_GRP_2_TX_QUEUE_NUM_PKTS_ENQUEUED_REG ():     
    return 0x0680024

def MAC_GRP_2_TX_QUEUE_NUM_PKTS_SENT_REG ():         
    return 0x0680028

def MAC_GRP_2_TX_QUEUE_NUM_WORDS_PUSHED_REG ():      
    return 0x068002c

def MAC_GRP_2_TX_QUEUE_NUM_BYTES_PUSHED_REG ():      
    return 0x0680030


# Name: nf2_mac_grp (MAC_GRP_3)
# Description: Ethernet MAC group
# File: lib/verilog/core/io_queues/ethernet_queue/xml/ethernet_mac.xml
def MAC_GRP_3_CONTROL_REG ():                        
    return 0x06c0000

def MAC_GRP_3_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():     
    return 0x06c0004

def MAC_GRP_3_RX_QUEUE_NUM_PKTS_STORED_REG ():       
    return 0x06c0008

def MAC_GRP_3_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG (): 
    return 0x06c000c

def MAC_GRP_3_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG ():  
    return 0x06c0010

def MAC_GRP_3_RX_QUEUE_NUM_PKTS_DEQUEUED_REG ():     
    return 0x06c0014

def MAC_GRP_3_RX_QUEUE_NUM_WORDS_PUSHED_REG ():      
    return 0x06c0018

def MAC_GRP_3_RX_QUEUE_NUM_BYTES_PUSHED_REG ():      
    return 0x06c001c

def MAC_GRP_3_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():     
    return 0x06c0020

def MAC_GRP_3_TX_QUEUE_NUM_PKTS_ENQUEUED_REG ():     
    return 0x06c0024

def MAC_GRP_3_TX_QUEUE_NUM_PKTS_SENT_REG ():         
    return 0x06c0028

def MAC_GRP_3_TX_QUEUE_NUM_WORDS_PUSHED_REG ():      
    return 0x06c002c

def MAC_GRP_3_TX_QUEUE_NUM_BYTES_PUSHED_REG ():      
    return 0x06c0030


# Name: cpu_dma_queue (CPU_QUEUE_0)
# Description: CPU DMA queue
# File: lib/verilog/core/io_queues/cpu_dma_queue/xml/cpu_dma_queue.xml
def CPU_QUEUE_0_CONTROL_REG ():                       
    return 0x0700000

def CPU_QUEUE_0_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():    
    return 0x0700004

def CPU_QUEUE_0_RX_QUEUE_NUM_PKTS_ENQUEUED_REG ():    
    return 0x0700008

def CPU_QUEUE_0_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG (): 
    return 0x070000c

def CPU_QUEUE_0_RX_QUEUE_NUM_PKTS_DEQUEUED_REG ():    
    return 0x0700010

def CPU_QUEUE_0_RX_QUEUE_NUM_UNDERRUNS_REG ():        
    return 0x0700014

def CPU_QUEUE_0_RX_QUEUE_NUM_OVERRUNS_REG ():         
    return 0x0700018

def CPU_QUEUE_0_RX_QUEUE_NUM_WORDS_PUSHED_REG ():     
    return 0x070001c

def CPU_QUEUE_0_RX_QUEUE_NUM_BYTES_PUSHED_REG ():     
    return 0x0700020

def CPU_QUEUE_0_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():    
    return 0x0700024

def CPU_QUEUE_0_TX_QUEUE_NUM_PKTS_ENQUEUED_REG ():    
    return 0x0700028

def CPU_QUEUE_0_TX_QUEUE_NUM_PKTS_DEQUEUED_REG ():    
    return 0x070002c

def CPU_QUEUE_0_TX_QUEUE_NUM_UNDERRUNS_REG ():        
    return 0x0700030

def CPU_QUEUE_0_TX_QUEUE_NUM_OVERRUNS_REG ():         
    return 0x0700034

def CPU_QUEUE_0_TX_QUEUE_NUM_WORDS_PUSHED_REG ():     
    return 0x0700038

def CPU_QUEUE_0_TX_QUEUE_NUM_BYTES_PUSHED_REG ():     
    return 0x070003c


# Name: cpu_dma_queue (CPU_QUEUE_1)
# Description: CPU DMA queue
# File: lib/verilog/core/io_queues/cpu_dma_queue/xml/cpu_dma_queue.xml
def CPU_QUEUE_1_CONTROL_REG ():                       
    return 0x0740000

def CPU_QUEUE_1_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():    
    return 0x0740004

def CPU_QUEUE_1_RX_QUEUE_NUM_PKTS_ENQUEUED_REG ():    
    return 0x0740008

def CPU_QUEUE_1_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG (): 
    return 0x074000c

def CPU_QUEUE_1_RX_QUEUE_NUM_PKTS_DEQUEUED_REG ():    
    return 0x0740010

def CPU_QUEUE_1_RX_QUEUE_NUM_UNDERRUNS_REG ():        
    return 0x0740014

def CPU_QUEUE_1_RX_QUEUE_NUM_OVERRUNS_REG ():         
    return 0x0740018

def CPU_QUEUE_1_RX_QUEUE_NUM_WORDS_PUSHED_REG ():     
    return 0x074001c

def CPU_QUEUE_1_RX_QUEUE_NUM_BYTES_PUSHED_REG ():     
    return 0x0740020

def CPU_QUEUE_1_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():    
    return 0x0740024

def CPU_QUEUE_1_TX_QUEUE_NUM_PKTS_ENQUEUED_REG ():    
    return 0x0740028

def CPU_QUEUE_1_TX_QUEUE_NUM_PKTS_DEQUEUED_REG ():    
    return 0x074002c

def CPU_QUEUE_1_TX_QUEUE_NUM_UNDERRUNS_REG ():        
    return 0x0740030

def CPU_QUEUE_1_TX_QUEUE_NUM_OVERRUNS_REG ():         
    return 0x0740034

def CPU_QUEUE_1_TX_QUEUE_NUM_WORDS_PUSHED_REG ():     
    return 0x0740038

def CPU_QUEUE_1_TX_QUEUE_NUM_BYTES_PUSHED_REG ():     
    return 0x074003c


# Name: cpu_dma_queue (CPU_QUEUE_2)
# Description: CPU DMA queue
# File: lib/verilog/core/io_queues/cpu_dma_queue/xml/cpu_dma_queue.xml
def CPU_QUEUE_2_CONTROL_REG ():                       
    return 0x0780000

def CPU_QUEUE_2_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():    
    return 0x0780004

def CPU_QUEUE_2_RX_QUEUE_NUM_PKTS_ENQUEUED_REG ():    
    return 0x0780008

def CPU_QUEUE_2_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG (): 
    return 0x078000c

def CPU_QUEUE_2_RX_QUEUE_NUM_PKTS_DEQUEUED_REG ():    
    return 0x0780010

def CPU_QUEUE_2_RX_QUEUE_NUM_UNDERRUNS_REG ():        
    return 0x0780014

def CPU_QUEUE_2_RX_QUEUE_NUM_OVERRUNS_REG ():         
    return 0x0780018

def CPU_QUEUE_2_RX_QUEUE_NUM_WORDS_PUSHED_REG ():     
    return 0x078001c

def CPU_QUEUE_2_RX_QUEUE_NUM_BYTES_PUSHED_REG ():     
    return 0x0780020

def CPU_QUEUE_2_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():    
    return 0x0780024

def CPU_QUEUE_2_TX_QUEUE_NUM_PKTS_ENQUEUED_REG ():    
    return 0x0780028

def CPU_QUEUE_2_TX_QUEUE_NUM_PKTS_DEQUEUED_REG ():    
    return 0x078002c

def CPU_QUEUE_2_TX_QUEUE_NUM_UNDERRUNS_REG ():        
    return 0x0780030

def CPU_QUEUE_2_TX_QUEUE_NUM_OVERRUNS_REG ():         
    return 0x0780034

def CPU_QUEUE_2_TX_QUEUE_NUM_WORDS_PUSHED_REG ():     
    return 0x0780038

def CPU_QUEUE_2_TX_QUEUE_NUM_BYTES_PUSHED_REG ():     
    return 0x078003c


# Name: cpu_dma_queue (CPU_QUEUE_3)
# Description: CPU DMA queue
# File: lib/verilog/core/io_queues/cpu_dma_queue/xml/cpu_dma_queue.xml
def CPU_QUEUE_3_CONTROL_REG ():                       
    return 0x07c0000

def CPU_QUEUE_3_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():    
    return 0x07c0004

def CPU_QUEUE_3_RX_QUEUE_NUM_PKTS_ENQUEUED_REG ():    
    return 0x07c0008

def CPU_QUEUE_3_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG (): 
    return 0x07c000c

def CPU_QUEUE_3_RX_QUEUE_NUM_PKTS_DEQUEUED_REG ():    
    return 0x07c0010

def CPU_QUEUE_3_RX_QUEUE_NUM_UNDERRUNS_REG ():        
    return 0x07c0014

def CPU_QUEUE_3_RX_QUEUE_NUM_OVERRUNS_REG ():         
    return 0x07c0018

def CPU_QUEUE_3_RX_QUEUE_NUM_WORDS_PUSHED_REG ():     
    return 0x07c001c

def CPU_QUEUE_3_RX_QUEUE_NUM_BYTES_PUSHED_REG ():     
    return 0x07c0020

def CPU_QUEUE_3_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG ():    
    return 0x07c0024

def CPU_QUEUE_3_TX_QUEUE_NUM_PKTS_ENQUEUED_REG ():    
    return 0x07c0028

def CPU_QUEUE_3_TX_QUEUE_NUM_PKTS_DEQUEUED_REG ():    
    return 0x07c002c

def CPU_QUEUE_3_TX_QUEUE_NUM_UNDERRUNS_REG ():        
    return 0x07c0030

def CPU_QUEUE_3_TX_QUEUE_NUM_OVERRUNS_REG ():         
    return 0x07c0034

def CPU_QUEUE_3_TX_QUEUE_NUM_WORDS_PUSHED_REG ():     
    return 0x07c0038

def CPU_QUEUE_3_TX_QUEUE_NUM_BYTES_PUSHED_REG ():     
    return 0x07c003c


# Name: SRAM (SRAM)
# Description: SRAM

# Name: openflow_output_port_lookup (OPENFLOW_LOOKUP)
# Description: Output Port Lookup for OpenFlow hardware datapath
# File: projects/openflow_switch/include/output_port_lookup.xml
def OPENFLOW_LOOKUP_WILDCARD_MISSES_REG ():    
    return 0x2000000

def OPENFLOW_LOOKUP_WILDCARD_HITS_REG ():      
    return 0x2000004

def OPENFLOW_LOOKUP_EXACT_MISSES_REG ():       
    return 0x2000008

def OPENFLOW_LOOKUP_EXACT_HITS_REG ():         
    return 0x200000c

def OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_0_REG (): 
    return 0x2000010

def OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_1_REG (): 
    return 0x2000014

def OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_2_REG (): 
    return 0x2000018

def OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_3_REG (): 
    return 0x200001c

def OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_4_REG (): 
    return 0x2000020

def OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_5_REG (): 
    return 0x2000024

def OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_6_REG (): 
    return 0x2000028

def OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_7_REG (): 
    return 0x200002c

def OPENFLOW_LOOKUP_DUMY_SOFTWARE_0_REG ():    
    return 0x2000030

def OPENFLOW_LOOKUP_DUMY_SOFTWARE_1_REG ():    
    return 0x2000034

def OPENFLOW_LOOKUP_TIMER_REG ():              
    return 0x2000038


# Name: in_arb (IN_ARB)
# Description: Round-robin input arbiter
# File: lib/verilog/core/input_arbiter/rr_input_arbiter/xml/rr_input_arbiter.xml
def IN_ARB_NUM_PKTS_SENT_REG ():      
    return 0x2000100

def IN_ARB_LAST_PKT_WORD_0_HI_REG (): 
    return 0x2000104

def IN_ARB_LAST_PKT_WORD_0_LO_REG (): 
    return 0x2000108

def IN_ARB_LAST_PKT_CTRL_0_REG ():    
    return 0x200010c

def IN_ARB_LAST_PKT_WORD_1_HI_REG (): 
    return 0x2000110

def IN_ARB_LAST_PKT_WORD_1_LO_REG (): 
    return 0x2000114

def IN_ARB_LAST_PKT_CTRL_1_REG ():    
    return 0x2000118

def IN_ARB_STATE_REG ():              
    return 0x200011c


# Name: vlan_remover (VLAN_REMOVER)
# Description: Remove vlan tag and ethtype if ethtype is vlan, and store them into module header
# File: projects/openflow_switch/include/vlan_remover.xml

# Name: opl_processor (OPL_PROCESSOR)
# Description: opl_processor
# File: projects/openflow_switch/include/opl_processor.xml

# Name: header_parser (HEADER_PARSER)
# Description: Chop ether/IP/UDP-TCP header into 11 tuples
# File: projects/openflow_switch/include/header_parser.xml

# Name: top_ddos (TOP_DDOS)
# Description: Registers for Clock controller Module
# File: projects/openflow_switch/include/top_ddos.xml
def TOP_DDOS_THRESHOLD_REG ():    
    return 0x20002c0

def TOP_DDOS_MAX_COUNT_REG ():    
    return 0x20002c4

def TOP_DDOS_CONTROL_MODE_REG (): 
    return 0x20002c8

def TOP_DDOS_FLUSH_SIGNAL_REG (): 
    return 0x20002cc

def TOP_DDOS_COUNT_1_REG ():      
    return 0x20002d0

def TOP_DDOS_SRC_IP_1_REG ():     
    return 0x20002d4

def TOP_DDOS_DETECTED_IP_REG ():  
    return 0x20002d8


# Name: bram_output_queues (BRAM_OQ)
# Description: BRAM-based output queues
# File: lib/verilog/core/output_queues/bram_output_queues/xml/bram_output_queues.xml
def BRAM_OQ_DISABLE_QUEUES_REG ():                 
    return 0x2000300

def BRAM_OQ_QUEUE_0_NUM_PKT_BYTES_RECEIVED_REG (): 
    return 0x2000380

def BRAM_OQ_QUEUE_0_NUM_PKTS_RECEIVED_REG ():      
    return 0x2000384

def BRAM_OQ_QUEUE_0_NUM_PKTS_DROPPED_REG ():       
    return 0x2000388

def BRAM_OQ_QUEUE_0_NUM_WORDS_IN_QUEUE_REG ():     
    return 0x200038c

def BRAM_OQ_QUEUE_1_NUM_PKT_BYTES_RECEIVED_REG (): 
    return 0x2000390

def BRAM_OQ_QUEUE_1_NUM_PKTS_RECEIVED_REG ():      
    return 0x2000394

def BRAM_OQ_QUEUE_1_NUM_PKTS_DROPPED_REG ():       
    return 0x2000398

def BRAM_OQ_QUEUE_1_NUM_WORDS_IN_QUEUE_REG ():     
    return 0x200039c

def BRAM_OQ_QUEUE_2_NUM_PKT_BYTES_RECEIVED_REG (): 
    return 0x20003a0

def BRAM_OQ_QUEUE_2_NUM_PKTS_RECEIVED_REG ():      
    return 0x20003a4

def BRAM_OQ_QUEUE_2_NUM_PKTS_DROPPED_REG ():       
    return 0x20003a8

def BRAM_OQ_QUEUE_2_NUM_WORDS_IN_QUEUE_REG ():     
    return 0x20003ac

def BRAM_OQ_QUEUE_3_NUM_PKT_BYTES_RECEIVED_REG (): 
    return 0x20003b0

def BRAM_OQ_QUEUE_3_NUM_PKTS_RECEIVED_REG ():      
    return 0x20003b4

def BRAM_OQ_QUEUE_3_NUM_PKTS_DROPPED_REG ():       
    return 0x20003b8

def BRAM_OQ_QUEUE_3_NUM_WORDS_IN_QUEUE_REG ():     
    return 0x20003bc

def BRAM_OQ_QUEUE_4_NUM_PKT_BYTES_RECEIVED_REG (): 
    return 0x20003c0

def BRAM_OQ_QUEUE_4_NUM_PKTS_RECEIVED_REG ():      
    return 0x20003c4

def BRAM_OQ_QUEUE_4_NUM_PKTS_DROPPED_REG ():       
    return 0x20003c8

def BRAM_OQ_QUEUE_4_NUM_WORDS_IN_QUEUE_REG ():     
    return 0x20003cc

def BRAM_OQ_QUEUE_5_NUM_PKT_BYTES_RECEIVED_REG (): 
    return 0x20003d0

def BRAM_OQ_QUEUE_5_NUM_PKTS_RECEIVED_REG ():      
    return 0x20003d4

def BRAM_OQ_QUEUE_5_NUM_PKTS_DROPPED_REG ():       
    return 0x20003d8

def BRAM_OQ_QUEUE_5_NUM_WORDS_IN_QUEUE_REG ():     
    return 0x20003dc

def BRAM_OQ_QUEUE_6_NUM_PKT_BYTES_RECEIVED_REG (): 
    return 0x20003e0

def BRAM_OQ_QUEUE_6_NUM_PKTS_RECEIVED_REG ():      
    return 0x20003e4

def BRAM_OQ_QUEUE_6_NUM_PKTS_DROPPED_REG ():       
    return 0x20003e8

def BRAM_OQ_QUEUE_6_NUM_WORDS_IN_QUEUE_REG ():     
    return 0x20003ec

def BRAM_OQ_QUEUE_7_NUM_PKT_BYTES_RECEIVED_REG (): 
    return 0x20003f0

def BRAM_OQ_QUEUE_7_NUM_PKTS_RECEIVED_REG ():      
    return 0x20003f4

def BRAM_OQ_QUEUE_7_NUM_PKTS_DROPPED_REG ():       
    return 0x20003f8

def BRAM_OQ_QUEUE_7_NUM_WORDS_IN_QUEUE_REG ():     
    return 0x20003fc


def BRAM_OQ_QUEUE_GROUP_BASE_ADDR ():
    return 0x2000380

def BRAM_OQ_QUEUE_GROUP_INST_OFFSET():
    return 0x0000010

# Name: watchdog (WDT)
# Description: Watchdog timer
# File: projects/openflow_switch/include/watchdog.xml
def WDT_ENABLE_FLG_REG (): 
    return 0x2000400

def WDT_COUNTER_REG ():    
    return 0x2000404


# Name: match_arbiter (MATCH_ARBITER)
# Description: Arbitration between exact and wildcard lookups results
# File: projects/openflow_switch/include/match_arbiter.xml

# Name: exact_match (EXACT_MATCH)
# Description: exact match lookup
# File: projects/openflow_switch/include/exact_match.xml

# Name: wildcard_match (OPENFLOW_WILDCARD_LOOKUP)
# Description: wildcard match lookup
# File: projects/openflow_switch/include/wildcard_match.xml
def OPENFLOW_WILDCARD_LOOKUP_ACTION_0_REG ():        
    return 0x2001000

def OPENFLOW_WILDCARD_LOOKUP_ACTION_1_REG ():        
    return 0x2001004

def OPENFLOW_WILDCARD_LOOKUP_ACTION_2_REG ():        
    return 0x2001008

def OPENFLOW_WILDCARD_LOOKUP_ACTION_3_REG ():        
    return 0x200100c

def OPENFLOW_WILDCARD_LOOKUP_ACTION_4_REG ():        
    return 0x2001010

def OPENFLOW_WILDCARD_LOOKUP_ACTION_5_REG ():        
    return 0x2001014

def OPENFLOW_WILDCARD_LOOKUP_ACTION_6_REG ():        
    return 0x2001018

def OPENFLOW_WILDCARD_LOOKUP_ACTION_7_REG ():        
    return 0x200101c

def OPENFLOW_WILDCARD_LOOKUP_ACTION_8_REG ():        
    return 0x2001020

def OPENFLOW_WILDCARD_LOOKUP_ACTION_9_REG ():        
    return 0x2001024

def OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_0_REG ():      
    return 0x2001028

def OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_1_REG ():      
    return 0x200102c

def OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_2_REG ():      
    return 0x2001030

def OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_3_REG ():      
    return 0x2001034

def OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_4_REG ():      
    return 0x2001038

def OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_5_REG ():      
    return 0x200103c

def OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_6_REG ():      
    return 0x2001040

def OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_7_REG ():      
    return 0x2001044

def OPENFLOW_WILDCARD_LOOKUP_CMP_0_REG ():           
    return 0x2001048

def OPENFLOW_WILDCARD_LOOKUP_CMP_1_REG ():           
    return 0x200104c

def OPENFLOW_WILDCARD_LOOKUP_CMP_2_REG ():           
    return 0x2001050

def OPENFLOW_WILDCARD_LOOKUP_CMP_3_REG ():           
    return 0x2001054

def OPENFLOW_WILDCARD_LOOKUP_CMP_4_REG ():           
    return 0x2001058

def OPENFLOW_WILDCARD_LOOKUP_CMP_5_REG ():           
    return 0x200105c

def OPENFLOW_WILDCARD_LOOKUP_CMP_6_REG ():           
    return 0x2001060

def OPENFLOW_WILDCARD_LOOKUP_CMP_7_REG ():           
    return 0x2001064

def OPENFLOW_WILDCARD_LOOKUP_READ_ADDR_REG ():       
    return 0x2001068

def OPENFLOW_WILDCARD_LOOKUP_WRITE_ADDR_REG ():      
    return 0x200106c

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_0_REG ():     
    return 0x2001070

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_1_REG ():     
    return 0x2001074

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_2_REG ():     
    return 0x2001078

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_3_REG ():     
    return 0x200107c

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_4_REG ():     
    return 0x2001080

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_5_REG ():     
    return 0x2001084

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_6_REG ():     
    return 0x2001088

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_7_REG ():     
    return 0x200108c

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_8_REG ():     
    return 0x2001090

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_9_REG ():     
    return 0x2001094

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_10_REG ():    
    return 0x2001098

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_11_REG ():    
    return 0x200109c

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_12_REG ():    
    return 0x20010a0

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_13_REG ():    
    return 0x20010a4

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_14_REG ():    
    return 0x20010a8

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_15_REG ():    
    return 0x20010ac

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_16_REG ():    
    return 0x20010b0

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_17_REG ():    
    return 0x20010b4

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_18_REG ():    
    return 0x20010b8

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_19_REG ():    
    return 0x20010bc

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_20_REG ():    
    return 0x20010c0

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_21_REG ():    
    return 0x20010c4

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_22_REG ():    
    return 0x20010c8

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_23_REG ():    
    return 0x20010cc

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_24_REG ():    
    return 0x20010d0

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_25_REG ():    
    return 0x20010d4

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_26_REG ():    
    return 0x20010d8

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_27_REG ():    
    return 0x20010dc

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_28_REG ():    
    return 0x20010e0

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_29_REG ():    
    return 0x20010e4

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_30_REG ():    
    return 0x20010e8

def OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_31_REG ():    
    return 0x20010ec

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_0_REG ():      
    return 0x20010f0

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_1_REG ():      
    return 0x20010f4

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_2_REG ():      
    return 0x20010f8

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_3_REG ():      
    return 0x20010fc

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_4_REG ():      
    return 0x2001100

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_5_REG ():      
    return 0x2001104

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_6_REG ():      
    return 0x2001108

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_7_REG ():      
    return 0x200110c

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_8_REG ():      
    return 0x2001110

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_9_REG ():      
    return 0x2001114

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_10_REG ():     
    return 0x2001118

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_11_REG ():     
    return 0x200111c

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_12_REG ():     
    return 0x2001120

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_13_REG ():     
    return 0x2001124

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_14_REG ():     
    return 0x2001128

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_15_REG ():     
    return 0x200112c

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_16_REG ():     
    return 0x2001130

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_17_REG ():     
    return 0x2001134

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_18_REG ():     
    return 0x2001138

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_19_REG ():     
    return 0x200113c

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_20_REG ():     
    return 0x2001140

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_21_REG ():     
    return 0x2001144

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_22_REG ():     
    return 0x2001148

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_23_REG ():     
    return 0x200114c

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_24_REG ():     
    return 0x2001150

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_25_REG ():     
    return 0x2001154

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_26_REG ():     
    return 0x2001158

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_27_REG ():     
    return 0x200115c

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_28_REG ():     
    return 0x2001160

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_29_REG ():     
    return 0x2001164

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_30_REG ():     
    return 0x2001168

def OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_31_REG ():     
    return 0x200116c

def OPENFLOW_WILDCARD_LOOKUP_DUMMY_1_REG ():         
    return 0x2001170

def OPENFLOW_WILDCARD_LOOKUP_DUMMY_2_REG ():         
    return 0x2001174

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_0_REG ():  
    return 0x2001178

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_1_REG ():  
    return 0x200117c

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_2_REG ():  
    return 0x2001180

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_3_REG ():  
    return 0x2001184

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_4_REG ():  
    return 0x2001188

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_5_REG ():  
    return 0x200118c

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_6_REG ():  
    return 0x2001190

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_7_REG ():  
    return 0x2001194

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_8_REG ():  
    return 0x2001198

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_9_REG ():  
    return 0x200119c

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_10_REG (): 
    return 0x20011a0

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_11_REG (): 
    return 0x20011a4

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_12_REG (): 
    return 0x20011a8

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_13_REG (): 
    return 0x20011ac

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_14_REG (): 
    return 0x20011b0

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_15_REG (): 
    return 0x20011b4

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_16_REG (): 
    return 0x20011b8

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_17_REG (): 
    return 0x20011bc

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_18_REG (): 
    return 0x20011c0

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_19_REG (): 
    return 0x20011c4

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_20_REG (): 
    return 0x20011c8

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_21_REG (): 
    return 0x20011cc

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_22_REG (): 
    return 0x20011d0

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_23_REG (): 
    return 0x20011d4

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_24_REG (): 
    return 0x20011d8

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_25_REG (): 
    return 0x20011dc

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_26_REG (): 
    return 0x20011e0

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_27_REG (): 
    return 0x20011e4

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_28_REG (): 
    return 0x20011e8

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_29_REG (): 
    return 0x20011ec

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_30_REG (): 
    return 0x20011f0

def OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_31_REG (): 
    return 0x20011f4


# Name: DRAM (DRAM)
# Description: DRAM



# -------------------------------------
#   Bitmasks
# -------------------------------------

# Type: dma_iface_ctrl
# Description: DMA interface control register
# File: lib/verilog/core/dma/xml/dma.xml

# Part 1: bit positions
def DMA_IFACE_CTRL_DISABLE_POS():
    return 0

def DMA_IFACE_CTRL_RESET_POS():
    return 1


# Part 2: masks/values
def DMA_IFACE_CTRL_DISABLE():
    return 0x001; 

def DMA_IFACE_CTRL_RESET():
    return 0x002; 


# Type: mii_ctrl
# Description: MII control register
# File: lib/verilog/core/io/mdio/xml/mdio.xml

# Part 1: bit positions
def MII_CTRL_RESET_POS():
    return 15

def MII_CTRL_INTERNAL_LOOPBACK_POS():
    return 14

def MII_CTRL_SPEED_SEL_LO_POS():
    return 13

def MII_CTRL_AUTONEG_ENABLE_POS():
    return 12

def MII_CTRL_PWR_DOWN_POS():
    return 11

def MII_CTRL_ISOLATE_POS():
    return 10

def MII_CTRL_RESTART_AUTONEG_POS():
    return 9

def MII_CTRL_DUPLEX_MODE_POS():
    return 8

def MII_CTRL_COLLISION_TEST_EN_POS():
    return 7

def MII_CTRL_SPEED_SEL_HI_POS():
    return 6


# Part 2: masks/values
def MII_CTRL_RESET():
    return 0x8000; 

def MII_CTRL_INTERNAL_LOOPBACK():
    return 0x4000; 

def MII_CTRL_SPEED_SEL_LO():
    return 0x2000; 

def MII_CTRL_AUTONEG_ENABLE():
    return 0x1000; 

def MII_CTRL_PWR_DOWN():
    return 0x0800; 

def MII_CTRL_ISOLATE():
    return 0x0400; 

def MII_CTRL_RESTART_AUTONEG():
    return 0x0200; 

def MII_CTRL_DUPLEX_MODE():
    return 0x0100; 

def MII_CTRL_COLLISION_TEST_EN():
    return 0x0080; 

def MII_CTRL_SPEED_SEL_HI():
    return 0x0040; 


# Type: mii_status
# Description: MII status register
# File: lib/verilog/core/io/mdio/xml/mdio.xml

# Part 1: bit positions
def MII_STATUS_100BASE_T4_CAPABLE_POS():
    return 15

def MII_STATUS_100BASE_X_FULL_DPLX_CAPABLE_POS():
    return 14

def MII_STATUS_100BASE_X_HALF_DPLX_CAPABLE_POS():
    return 13

def MII_STATUS_10BASE_T_FULL_DPLX_CAPABLE_POS():
    return 12

def MII_STATUS_10BASE_T_HALF_DPLX_CAPABLE_POS():
    return 11

def MII_STATUS_10BASE_T2_FULL_DPLX_CAPABLE_POS():
    return 10

def MII_STATUS_10BASE_T2_HALF_DPLX_CAPABLE_POS():
    return 9

def MII_STATUS_EXTENDED_STATUS_POS():
    return 8

def MII_STATUS_MF_PREAMBLE_SUPPRESS_POS():
    return 6

def MII_STATUS_AUTONEG_COMPLETE_POS():
    return 5

def MII_STATUS_REMOTE_FAULT_POS():
    return 4

def MII_STATUS_AUTONEG_ABILITY_POS():
    return 3

def MII_STATUS_LINK_STATUS_POS():
    return 2

def MII_STATUS_JABBER_DETECT_POS():
    return 1

def MII_STATUS_EXTENDED_CAPABILITY_POS():
    return 0


# Part 2: masks/values
def MII_STATUS_100BASE_T4_CAPABLE():
    return 0x8000; 

def MII_STATUS_100BASE_X_FULL_DPLX_CAPABLE():
    return 0x4000; 

def MII_STATUS_100BASE_X_HALF_DPLX_CAPABLE():
    return 0x2000; 

def MII_STATUS_10BASE_T_FULL_DPLX_CAPABLE():
    return 0x1000; 

def MII_STATUS_10BASE_T_HALF_DPLX_CAPABLE():
    return 0x0800; 

def MII_STATUS_10BASE_T2_FULL_DPLX_CAPABLE():
    return 0x0400; 

def MII_STATUS_10BASE_T2_HALF_DPLX_CAPABLE():
    return 0x0200; 

def MII_STATUS_EXTENDED_STATUS():
    return 0x0100; 

def MII_STATUS_MF_PREAMBLE_SUPPRESS():
    return 0x0040; 

def MII_STATUS_AUTONEG_COMPLETE():
    return 0x0020; 

def MII_STATUS_REMOTE_FAULT():
    return 0x0010; 

def MII_STATUS_AUTONEG_ABILITY():
    return 0x0008; 

def MII_STATUS_LINK_STATUS():
    return 0x0004; 

def MII_STATUS_JABBER_DETECT():
    return 0x0002; 

def MII_STATUS_EXTENDED_CAPABILITY():
    return 0x0001; 


# Type: cpu_queue_control
# Description: DMA queue control register
# File: lib/verilog/core/io_queues/cpu_dma_queue/xml/cpu_dma_queue.xml

# Part 1: bit positions
def CPU_QUEUE_CONTROL_TX_QUEUE_DISABLE_POS():
    return 0

def CPU_QUEUE_CONTROL_RX_QUEUE_DISABLE_POS():
    return 1


# Part 2: masks/values
def CPU_QUEUE_CONTROL_TX_QUEUE_DISABLE():
    return 0x001; 

def CPU_QUEUE_CONTROL_RX_QUEUE_DISABLE():
    return 0x002; 


# Type: mac_grp_control
# Description: MAC group control register
# File: lib/verilog/core/io_queues/ethernet_queue/xml/ethernet_mac.xml

# Part 1: bit positions
def MAC_GRP_CONTROL_TX_QUEUE_DISABLE_POS():
    return 0

def MAC_GRP_CONTROL_RX_QUEUE_DISABLE_POS():
    return 1

def MAC_GRP_CONTROL_RESET_MAC_POS():
    return 2

def MAC_GRP_CONTROL_MAC_DISABLE_TX_POS():
    return 3

def MAC_GRP_CONTROL_MAC_DISABLE_RX_POS():
    return 4

def MAC_GRP_CONTROL_MAC_DISABLE_JUMBO_TX_POS():
    return 5

def MAC_GRP_CONTROL_MAC_DISABLE_JUMBO_RX_POS():
    return 6

def MAC_GRP_CONTROL_MAC_DISABLE_CRC_CHECK_POS():
    return 7

def MAC_GRP_CONTROL_MAC_DISABLE_CRC_GEN_POS():
    return 8


# Part 2: masks/values
def MAC_GRP_CONTROL_TX_QUEUE_DISABLE():
    return 0x001; 

def MAC_GRP_CONTROL_RX_QUEUE_DISABLE():
    return 0x002; 

def MAC_GRP_CONTROL_RESET_MAC():
    return 0x004; 

def MAC_GRP_CONTROL_MAC_DISABLE_TX():
    return 0x008; 

def MAC_GRP_CONTROL_MAC_DISABLE_RX():
    return 0x010; 

def MAC_GRP_CONTROL_MAC_DISABLE_JUMBO_TX():
    return 0x020; 

def MAC_GRP_CONTROL_MAC_DISABLE_JUMBO_RX():
    return 0x040; 

def MAC_GRP_CONTROL_MAC_DISABLE_CRC_CHECK():
    return 0x080; 

def MAC_GRP_CONTROL_MAC_DISABLE_CRC_GEN():
    return 0x100; 




# -------------------------------------
#   Register map
# -------------------------------------

import __main__;
if 'nf_regmap' not in dir(__main__):
    __main__.nf_regmap = {}

__main__.nf_regmap.update({
    0x0400000 : "DEV_ID_MD5_0_REG",
    0x0400004 : "DEV_ID_MD5_1_REG",
    0x0400008 : "DEV_ID_MD5_2_REG",
    0x040000c : "DEV_ID_MD5_3_REG",
    0x0400010 : "DEV_ID_DEVICE_ID_REG",
    0x0400014 : "DEV_ID_VERSION_REG",
    0x0400018 : "DEV_ID_CPCI_ID_REG",
    0x040001c : "DEV_ID_PROJ_DIR_0_REG",
    0x0400020 : "DEV_ID_PROJ_DIR_1_REG",
    0x0400024 : "DEV_ID_PROJ_DIR_2_REG",
    0x0400028 : "DEV_ID_PROJ_DIR_3_REG",
    0x040002c : "DEV_ID_PROJ_DIR_4_REG",
    0x0400030 : "DEV_ID_PROJ_DIR_5_REG",
    0x0400034 : "DEV_ID_PROJ_DIR_6_REG",
    0x0400038 : "DEV_ID_PROJ_DIR_7_REG",
    0x040003c : "DEV_ID_PROJ_DIR_8_REG",
    0x0400040 : "DEV_ID_PROJ_DIR_9_REG",
    0x0400044 : "DEV_ID_PROJ_DIR_10_REG",
    0x0400048 : "DEV_ID_PROJ_DIR_11_REG",
    0x040004c : "DEV_ID_PROJ_DIR_12_REG",
    0x0400050 : "DEV_ID_PROJ_DIR_13_REG",
    0x0400054 : "DEV_ID_PROJ_DIR_14_REG",
    0x0400058 : "DEV_ID_PROJ_DIR_15_REG",
    0x040005c : "DEV_ID_PROJ_NAME_0_REG",
    0x0400060 : "DEV_ID_PROJ_NAME_1_REG",
    0x0400064 : "DEV_ID_PROJ_NAME_2_REG",
    0x0400068 : "DEV_ID_PROJ_NAME_3_REG",
    0x040006c : "DEV_ID_PROJ_NAME_4_REG",
    0x0400070 : "DEV_ID_PROJ_NAME_5_REG",
    0x0400074 : "DEV_ID_PROJ_NAME_6_REG",
    0x0400078 : "DEV_ID_PROJ_NAME_7_REG",
    0x040007c : "DEV_ID_PROJ_NAME_8_REG",
    0x0400080 : "DEV_ID_PROJ_NAME_9_REG",
    0x0400084 : "DEV_ID_PROJ_NAME_10_REG",
    0x0400088 : "DEV_ID_PROJ_NAME_11_REG",
    0x040008c : "DEV_ID_PROJ_NAME_12_REG",
    0x0400090 : "DEV_ID_PROJ_NAME_13_REG",
    0x0400094 : "DEV_ID_PROJ_NAME_14_REG",
    0x0400098 : "DEV_ID_PROJ_NAME_15_REG",
    0x040009c : "DEV_ID_PROJ_DESC_0_REG",
    0x04000a0 : "DEV_ID_PROJ_DESC_1_REG",
    0x04000a4 : "DEV_ID_PROJ_DESC_2_REG",
    0x04000a8 : "DEV_ID_PROJ_DESC_3_REG",
    0x04000ac : "DEV_ID_PROJ_DESC_4_REG",
    0x04000b0 : "DEV_ID_PROJ_DESC_5_REG",
    0x04000b4 : "DEV_ID_PROJ_DESC_6_REG",
    0x04000b8 : "DEV_ID_PROJ_DESC_7_REG",
    0x04000bc : "DEV_ID_PROJ_DESC_8_REG",
    0x04000c0 : "DEV_ID_PROJ_DESC_9_REG",
    0x04000c4 : "DEV_ID_PROJ_DESC_10_REG",
    0x04000c8 : "DEV_ID_PROJ_DESC_11_REG",
    0x04000cc : "DEV_ID_PROJ_DESC_12_REG",
    0x04000d0 : "DEV_ID_PROJ_DESC_13_REG",
    0x04000d4 : "DEV_ID_PROJ_DESC_14_REG",
    0x04000d8 : "DEV_ID_PROJ_DESC_15_REG",
    0x04000dc : "DEV_ID_PROJ_DESC_16_REG",
    0x04000e0 : "DEV_ID_PROJ_DESC_17_REG",
    0x04000e4 : "DEV_ID_PROJ_DESC_18_REG",
    0x04000e8 : "DEV_ID_PROJ_DESC_19_REG",
    0x04000ec : "DEV_ID_PROJ_DESC_20_REG",
    0x04000f0 : "DEV_ID_PROJ_DESC_21_REG",
    0x04000f4 : "DEV_ID_PROJ_DESC_22_REG",
    0x04000f8 : "DEV_ID_PROJ_DESC_23_REG",
    0x04000fc : "DEV_ID_PROJ_DESC_24_REG",

    0x0440000 : "MDIO_PHY_0_CONTROL_REG",
    0x0440004 : "MDIO_PHY_0_STATUS_REG",
    0x0440008 : "MDIO_PHY_0_PHY_ID_HI_REG",
    0x044000c : "MDIO_PHY_0_PHY_ID_LO_REG",
    0x0440010 : "MDIO_PHY_0_AUTONEGOTIATION_ADVERT_REG",
    0x0440014 : "MDIO_PHY_0_AUTONEG_LINK_PARTNER_BASE_PAGE_ABILITY_REG",
    0x0440018 : "MDIO_PHY_0_AUTONEG_EXPANSION_REG",
    0x044001c : "MDIO_PHY_0_AUTONEG_NEXT_PAGE_TX_REG",
    0x0440020 : "MDIO_PHY_0_AUTONEG_LINK_PARTNER_RCVD_NEXT_PAGE_REG",
    0x0440024 : "MDIO_PHY_0_MASTER_SLAVE_CTRL_REG",
    0x0440028 : "MDIO_PHY_0_MASTER_SLAVE_STATUS_REG",
    0x044002c : "MDIO_PHY_0_PSE_CTRL_REG",
    0x0440030 : "MDIO_PHY_0_PSE_STATUS_REG",
    0x0440034 : "MDIO_PHY_0_MMD_ACCESS_CTRL_REG",
    0x0440038 : "MDIO_PHY_0_MMD_ACCESS_STATUS_REG",
    0x044003c : "MDIO_PHY_0_EXTENDED_STATUS_REG",
    0x0440040 : "MDIO_PHY_0_PHY_EXTENDED_CTRL_REG",
    0x0440044 : "MDIO_PHY_0_PHY_EXTENDED_STATUS_REG",
    0x0440048 : "MDIO_PHY_0_RX_ERROR_COUNT_REG",
    0x044004c : "MDIO_PHY_0_FALSE_CARRIER_SENSE_COUNT_REG",
    0x0440050 : "MDIO_PHY_0_RX_NOT_OK_COUNT_REG",
    0x0440054 : "MDIO_PHY_0_EXPANSION_1_REG",
    0x0440058 : "MDIO_PHY_0_EXPANSION_2_REG",
    0x044005c : "MDIO_PHY_0_EXPANSION_REG_ACCESS_REG",
    0x0440060 : "MDIO_PHY_0_SHADOW_18_REG",
    0x0440064 : "MDIO_PHY_0_AUX_STATUS_REG",
    0x0440068 : "MDIO_PHY_0_INT_STATUS_REG",
    0x044006c : "MDIO_PHY_0_INT_MASK_REG",
    0x0440070 : "MDIO_PHY_0_SHADOW_1C_REG",
    0x0440074 : "MDIO_PHY_0_SHADOW_1D_REG",
    0x0440078 : "MDIO_PHY_0_TEST_REG",
    0x044007c : "MDIO_PHY_0_RESERVED_REG",
    0x0440080 : "MDIO_PHY_1_CONTROL_REG",
    0x0440084 : "MDIO_PHY_1_STATUS_REG",
    0x0440088 : "MDIO_PHY_1_PHY_ID_HI_REG",
    0x044008c : "MDIO_PHY_1_PHY_ID_LO_REG",
    0x0440090 : "MDIO_PHY_1_AUTONEGOTIATION_ADVERT_REG",
    0x0440094 : "MDIO_PHY_1_AUTONEG_LINK_PARTNER_BASE_PAGE_ABILITY_REG",
    0x0440098 : "MDIO_PHY_1_AUTONEG_EXPANSION_REG",
    0x044009c : "MDIO_PHY_1_AUTONEG_NEXT_PAGE_TX_REG",
    0x04400a0 : "MDIO_PHY_1_AUTONEG_LINK_PARTNER_RCVD_NEXT_PAGE_REG",
    0x04400a4 : "MDIO_PHY_1_MASTER_SLAVE_CTRL_REG",
    0x04400a8 : "MDIO_PHY_1_MASTER_SLAVE_STATUS_REG",
    0x04400ac : "MDIO_PHY_1_PSE_CTRL_REG",
    0x04400b0 : "MDIO_PHY_1_PSE_STATUS_REG",
    0x04400b4 : "MDIO_PHY_1_MMD_ACCESS_CTRL_REG",
    0x04400b8 : "MDIO_PHY_1_MMD_ACCESS_STATUS_REG",
    0x04400bc : "MDIO_PHY_1_EXTENDED_STATUS_REG",
    0x04400c0 : "MDIO_PHY_1_PHY_EXTENDED_CTRL_REG",
    0x04400c4 : "MDIO_PHY_1_PHY_EXTENDED_STATUS_REG",
    0x04400c8 : "MDIO_PHY_1_RX_ERROR_COUNT_REG",
    0x04400cc : "MDIO_PHY_1_FALSE_CARRIER_SENSE_COUNT_REG",
    0x04400d0 : "MDIO_PHY_1_RX_NOT_OK_COUNT_REG",
    0x04400d4 : "MDIO_PHY_1_EXPANSION_1_REG",
    0x04400d8 : "MDIO_PHY_1_EXPANSION_2_REG",
    0x04400dc : "MDIO_PHY_1_EXPANSION_REG_ACCESS_REG",
    0x04400e0 : "MDIO_PHY_1_SHADOW_18_REG",
    0x04400e4 : "MDIO_PHY_1_AUX_STATUS_REG",
    0x04400e8 : "MDIO_PHY_1_INT_STATUS_REG",
    0x04400ec : "MDIO_PHY_1_INT_MASK_REG",
    0x04400f0 : "MDIO_PHY_1_SHADOW_1C_REG",
    0x04400f4 : "MDIO_PHY_1_SHADOW_1D_REG",
    0x04400f8 : "MDIO_PHY_1_TEST_REG",
    0x04400fc : "MDIO_PHY_1_RESERVED_REG",
    0x0440100 : "MDIO_PHY_2_CONTROL_REG",
    0x0440104 : "MDIO_PHY_2_STATUS_REG",
    0x0440108 : "MDIO_PHY_2_PHY_ID_HI_REG",
    0x044010c : "MDIO_PHY_2_PHY_ID_LO_REG",
    0x0440110 : "MDIO_PHY_2_AUTONEGOTIATION_ADVERT_REG",
    0x0440114 : "MDIO_PHY_2_AUTONEG_LINK_PARTNER_BASE_PAGE_ABILITY_REG",
    0x0440118 : "MDIO_PHY_2_AUTONEG_EXPANSION_REG",
    0x044011c : "MDIO_PHY_2_AUTONEG_NEXT_PAGE_TX_REG",
    0x0440120 : "MDIO_PHY_2_AUTONEG_LINK_PARTNER_RCVD_NEXT_PAGE_REG",
    0x0440124 : "MDIO_PHY_2_MASTER_SLAVE_CTRL_REG",
    0x0440128 : "MDIO_PHY_2_MASTER_SLAVE_STATUS_REG",
    0x044012c : "MDIO_PHY_2_PSE_CTRL_REG",
    0x0440130 : "MDIO_PHY_2_PSE_STATUS_REG",
    0x0440134 : "MDIO_PHY_2_MMD_ACCESS_CTRL_REG",
    0x0440138 : "MDIO_PHY_2_MMD_ACCESS_STATUS_REG",
    0x044013c : "MDIO_PHY_2_EXTENDED_STATUS_REG",
    0x0440140 : "MDIO_PHY_2_PHY_EXTENDED_CTRL_REG",
    0x0440144 : "MDIO_PHY_2_PHY_EXTENDED_STATUS_REG",
    0x0440148 : "MDIO_PHY_2_RX_ERROR_COUNT_REG",
    0x044014c : "MDIO_PHY_2_FALSE_CARRIER_SENSE_COUNT_REG",
    0x0440150 : "MDIO_PHY_2_RX_NOT_OK_COUNT_REG",
    0x0440154 : "MDIO_PHY_2_EXPANSION_1_REG",
    0x0440158 : "MDIO_PHY_2_EXPANSION_2_REG",
    0x044015c : "MDIO_PHY_2_EXPANSION_REG_ACCESS_REG",
    0x0440160 : "MDIO_PHY_2_SHADOW_18_REG",
    0x0440164 : "MDIO_PHY_2_AUX_STATUS_REG",
    0x0440168 : "MDIO_PHY_2_INT_STATUS_REG",
    0x044016c : "MDIO_PHY_2_INT_MASK_REG",
    0x0440170 : "MDIO_PHY_2_SHADOW_1C_REG",
    0x0440174 : "MDIO_PHY_2_SHADOW_1D_REG",
    0x0440178 : "MDIO_PHY_2_TEST_REG",
    0x044017c : "MDIO_PHY_2_RESERVED_REG",
    0x0440180 : "MDIO_PHY_3_CONTROL_REG",
    0x0440184 : "MDIO_PHY_3_STATUS_REG",
    0x0440188 : "MDIO_PHY_3_PHY_ID_HI_REG",
    0x044018c : "MDIO_PHY_3_PHY_ID_LO_REG",
    0x0440190 : "MDIO_PHY_3_AUTONEGOTIATION_ADVERT_REG",
    0x0440194 : "MDIO_PHY_3_AUTONEG_LINK_PARTNER_BASE_PAGE_ABILITY_REG",
    0x0440198 : "MDIO_PHY_3_AUTONEG_EXPANSION_REG",
    0x044019c : "MDIO_PHY_3_AUTONEG_NEXT_PAGE_TX_REG",
    0x04401a0 : "MDIO_PHY_3_AUTONEG_LINK_PARTNER_RCVD_NEXT_PAGE_REG",
    0x04401a4 : "MDIO_PHY_3_MASTER_SLAVE_CTRL_REG",
    0x04401a8 : "MDIO_PHY_3_MASTER_SLAVE_STATUS_REG",
    0x04401ac : "MDIO_PHY_3_PSE_CTRL_REG",
    0x04401b0 : "MDIO_PHY_3_PSE_STATUS_REG",
    0x04401b4 : "MDIO_PHY_3_MMD_ACCESS_CTRL_REG",
    0x04401b8 : "MDIO_PHY_3_MMD_ACCESS_STATUS_REG",
    0x04401bc : "MDIO_PHY_3_EXTENDED_STATUS_REG",
    0x04401c0 : "MDIO_PHY_3_PHY_EXTENDED_CTRL_REG",
    0x04401c4 : "MDIO_PHY_3_PHY_EXTENDED_STATUS_REG",
    0x04401c8 : "MDIO_PHY_3_RX_ERROR_COUNT_REG",
    0x04401cc : "MDIO_PHY_3_FALSE_CARRIER_SENSE_COUNT_REG",
    0x04401d0 : "MDIO_PHY_3_RX_NOT_OK_COUNT_REG",
    0x04401d4 : "MDIO_PHY_3_EXPANSION_1_REG",
    0x04401d8 : "MDIO_PHY_3_EXPANSION_2_REG",
    0x04401dc : "MDIO_PHY_3_EXPANSION_REG_ACCESS_REG",
    0x04401e0 : "MDIO_PHY_3_SHADOW_18_REG",
    0x04401e4 : "MDIO_PHY_3_AUX_STATUS_REG",
    0x04401e8 : "MDIO_PHY_3_INT_STATUS_REG",
    0x04401ec : "MDIO_PHY_3_INT_MASK_REG",
    0x04401f0 : "MDIO_PHY_3_SHADOW_1C_REG",
    0x04401f4 : "MDIO_PHY_3_SHADOW_1D_REG",
    0x04401f8 : "MDIO_PHY_3_TEST_REG",
    0x04401fc : "MDIO_PHY_3_RESERVED_REG",

    0x0500000 : "DMA_CTRL_REG",
    0x0500004 : "DMA_NUM_INGRESS_PKTS_REG",
    0x0500008 : "DMA_NUM_INGRESS_BYTES_REG",
    0x050000c : "DMA_NUM_EGRESS_PKTS_REG",
    0x0500010 : "DMA_NUM_EGRESS_BYTES_REG",
    0x0500014 : "DMA_NUM_TIMEOUTS_REG",

    0x0600000 : "MAC_GRP_0_CONTROL_REG",
    0x0600004 : "MAC_GRP_0_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0600008 : "MAC_GRP_0_RX_QUEUE_NUM_PKTS_STORED_REG",
    0x060000c : "MAC_GRP_0_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG",
    0x0600010 : "MAC_GRP_0_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG",
    0x0600014 : "MAC_GRP_0_RX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x0600018 : "MAC_GRP_0_RX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x060001c : "MAC_GRP_0_RX_QUEUE_NUM_BYTES_PUSHED_REG",
    0x0600020 : "MAC_GRP_0_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0600024 : "MAC_GRP_0_TX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x0600028 : "MAC_GRP_0_TX_QUEUE_NUM_PKTS_SENT_REG",
    0x060002c : "MAC_GRP_0_TX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x0600030 : "MAC_GRP_0_TX_QUEUE_NUM_BYTES_PUSHED_REG",

    0x0640000 : "MAC_GRP_1_CONTROL_REG",
    0x0640004 : "MAC_GRP_1_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0640008 : "MAC_GRP_1_RX_QUEUE_NUM_PKTS_STORED_REG",
    0x064000c : "MAC_GRP_1_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG",
    0x0640010 : "MAC_GRP_1_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG",
    0x0640014 : "MAC_GRP_1_RX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x0640018 : "MAC_GRP_1_RX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x064001c : "MAC_GRP_1_RX_QUEUE_NUM_BYTES_PUSHED_REG",
    0x0640020 : "MAC_GRP_1_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0640024 : "MAC_GRP_1_TX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x0640028 : "MAC_GRP_1_TX_QUEUE_NUM_PKTS_SENT_REG",
    0x064002c : "MAC_GRP_1_TX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x0640030 : "MAC_GRP_1_TX_QUEUE_NUM_BYTES_PUSHED_REG",

    0x0680000 : "MAC_GRP_2_CONTROL_REG",
    0x0680004 : "MAC_GRP_2_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0680008 : "MAC_GRP_2_RX_QUEUE_NUM_PKTS_STORED_REG",
    0x068000c : "MAC_GRP_2_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG",
    0x0680010 : "MAC_GRP_2_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG",
    0x0680014 : "MAC_GRP_2_RX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x0680018 : "MAC_GRP_2_RX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x068001c : "MAC_GRP_2_RX_QUEUE_NUM_BYTES_PUSHED_REG",
    0x0680020 : "MAC_GRP_2_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0680024 : "MAC_GRP_2_TX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x0680028 : "MAC_GRP_2_TX_QUEUE_NUM_PKTS_SENT_REG",
    0x068002c : "MAC_GRP_2_TX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x0680030 : "MAC_GRP_2_TX_QUEUE_NUM_BYTES_PUSHED_REG",

    0x06c0000 : "MAC_GRP_3_CONTROL_REG",
    0x06c0004 : "MAC_GRP_3_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x06c0008 : "MAC_GRP_3_RX_QUEUE_NUM_PKTS_STORED_REG",
    0x06c000c : "MAC_GRP_3_RX_QUEUE_NUM_PKTS_DROPPED_FULL_REG",
    0x06c0010 : "MAC_GRP_3_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG",
    0x06c0014 : "MAC_GRP_3_RX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x06c0018 : "MAC_GRP_3_RX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x06c001c : "MAC_GRP_3_RX_QUEUE_NUM_BYTES_PUSHED_REG",
    0x06c0020 : "MAC_GRP_3_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x06c0024 : "MAC_GRP_3_TX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x06c0028 : "MAC_GRP_3_TX_QUEUE_NUM_PKTS_SENT_REG",
    0x06c002c : "MAC_GRP_3_TX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x06c0030 : "MAC_GRP_3_TX_QUEUE_NUM_BYTES_PUSHED_REG",

    0x0700000 : "CPU_QUEUE_0_CONTROL_REG",
    0x0700004 : "CPU_QUEUE_0_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0700008 : "CPU_QUEUE_0_RX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x070000c : "CPU_QUEUE_0_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG",
    0x0700010 : "CPU_QUEUE_0_RX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x0700014 : "CPU_QUEUE_0_RX_QUEUE_NUM_UNDERRUNS_REG",
    0x0700018 : "CPU_QUEUE_0_RX_QUEUE_NUM_OVERRUNS_REG",
    0x070001c : "CPU_QUEUE_0_RX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x0700020 : "CPU_QUEUE_0_RX_QUEUE_NUM_BYTES_PUSHED_REG",
    0x0700024 : "CPU_QUEUE_0_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0700028 : "CPU_QUEUE_0_TX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x070002c : "CPU_QUEUE_0_TX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x0700030 : "CPU_QUEUE_0_TX_QUEUE_NUM_UNDERRUNS_REG",
    0x0700034 : "CPU_QUEUE_0_TX_QUEUE_NUM_OVERRUNS_REG",
    0x0700038 : "CPU_QUEUE_0_TX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x070003c : "CPU_QUEUE_0_TX_QUEUE_NUM_BYTES_PUSHED_REG",

    0x0740000 : "CPU_QUEUE_1_CONTROL_REG",
    0x0740004 : "CPU_QUEUE_1_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0740008 : "CPU_QUEUE_1_RX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x074000c : "CPU_QUEUE_1_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG",
    0x0740010 : "CPU_QUEUE_1_RX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x0740014 : "CPU_QUEUE_1_RX_QUEUE_NUM_UNDERRUNS_REG",
    0x0740018 : "CPU_QUEUE_1_RX_QUEUE_NUM_OVERRUNS_REG",
    0x074001c : "CPU_QUEUE_1_RX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x0740020 : "CPU_QUEUE_1_RX_QUEUE_NUM_BYTES_PUSHED_REG",
    0x0740024 : "CPU_QUEUE_1_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0740028 : "CPU_QUEUE_1_TX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x074002c : "CPU_QUEUE_1_TX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x0740030 : "CPU_QUEUE_1_TX_QUEUE_NUM_UNDERRUNS_REG",
    0x0740034 : "CPU_QUEUE_1_TX_QUEUE_NUM_OVERRUNS_REG",
    0x0740038 : "CPU_QUEUE_1_TX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x074003c : "CPU_QUEUE_1_TX_QUEUE_NUM_BYTES_PUSHED_REG",

    0x0780000 : "CPU_QUEUE_2_CONTROL_REG",
    0x0780004 : "CPU_QUEUE_2_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0780008 : "CPU_QUEUE_2_RX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x078000c : "CPU_QUEUE_2_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG",
    0x0780010 : "CPU_QUEUE_2_RX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x0780014 : "CPU_QUEUE_2_RX_QUEUE_NUM_UNDERRUNS_REG",
    0x0780018 : "CPU_QUEUE_2_RX_QUEUE_NUM_OVERRUNS_REG",
    0x078001c : "CPU_QUEUE_2_RX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x0780020 : "CPU_QUEUE_2_RX_QUEUE_NUM_BYTES_PUSHED_REG",
    0x0780024 : "CPU_QUEUE_2_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x0780028 : "CPU_QUEUE_2_TX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x078002c : "CPU_QUEUE_2_TX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x0780030 : "CPU_QUEUE_2_TX_QUEUE_NUM_UNDERRUNS_REG",
    0x0780034 : "CPU_QUEUE_2_TX_QUEUE_NUM_OVERRUNS_REG",
    0x0780038 : "CPU_QUEUE_2_TX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x078003c : "CPU_QUEUE_2_TX_QUEUE_NUM_BYTES_PUSHED_REG",

    0x07c0000 : "CPU_QUEUE_3_CONTROL_REG",
    0x07c0004 : "CPU_QUEUE_3_RX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x07c0008 : "CPU_QUEUE_3_RX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x07c000c : "CPU_QUEUE_3_RX_QUEUE_NUM_PKTS_DROPPED_BAD_REG",
    0x07c0010 : "CPU_QUEUE_3_RX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x07c0014 : "CPU_QUEUE_3_RX_QUEUE_NUM_UNDERRUNS_REG",
    0x07c0018 : "CPU_QUEUE_3_RX_QUEUE_NUM_OVERRUNS_REG",
    0x07c001c : "CPU_QUEUE_3_RX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x07c0020 : "CPU_QUEUE_3_RX_QUEUE_NUM_BYTES_PUSHED_REG",
    0x07c0024 : "CPU_QUEUE_3_TX_QUEUE_NUM_PKTS_IN_QUEUE_REG",
    0x07c0028 : "CPU_QUEUE_3_TX_QUEUE_NUM_PKTS_ENQUEUED_REG",
    0x07c002c : "CPU_QUEUE_3_TX_QUEUE_NUM_PKTS_DEQUEUED_REG",
    0x07c0030 : "CPU_QUEUE_3_TX_QUEUE_NUM_UNDERRUNS_REG",
    0x07c0034 : "CPU_QUEUE_3_TX_QUEUE_NUM_OVERRUNS_REG",
    0x07c0038 : "CPU_QUEUE_3_TX_QUEUE_NUM_WORDS_PUSHED_REG",
    0x07c003c : "CPU_QUEUE_3_TX_QUEUE_NUM_BYTES_PUSHED_REG",

    0x2000000 : "OPENFLOW_LOOKUP_WILDCARD_MISSES_REG",
    0x2000004 : "OPENFLOW_LOOKUP_WILDCARD_HITS_REG",
    0x2000008 : "OPENFLOW_LOOKUP_EXACT_MISSES_REG",
    0x200000c : "OPENFLOW_LOOKUP_EXACT_HITS_REG",
    0x2000010 : "OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_0_REG",
    0x2000014 : "OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_1_REG",
    0x2000018 : "OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_2_REG",
    0x200001c : "OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_3_REG",
    0x2000020 : "OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_4_REG",
    0x2000024 : "OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_5_REG",
    0x2000028 : "OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_6_REG",
    0x200002c : "OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_7_REG",
    0x2000030 : "OPENFLOW_LOOKUP_DUMY_SOFTWARE_0_REG",
    0x2000034 : "OPENFLOW_LOOKUP_DUMY_SOFTWARE_1_REG",
    0x2000038 : "OPENFLOW_LOOKUP_TIMER_REG",

    0x2000100 : "IN_ARB_NUM_PKTS_SENT_REG",
    0x2000104 : "IN_ARB_LAST_PKT_WORD_0_HI_REG",
    0x2000108 : "IN_ARB_LAST_PKT_WORD_0_LO_REG",
    0x200010c : "IN_ARB_LAST_PKT_CTRL_0_REG",
    0x2000110 : "IN_ARB_LAST_PKT_WORD_1_HI_REG",
    0x2000114 : "IN_ARB_LAST_PKT_WORD_1_LO_REG",
    0x2000118 : "IN_ARB_LAST_PKT_CTRL_1_REG",
    0x200011c : "IN_ARB_STATE_REG",

    0x20002c0 : "TOP_DDOS_THRESHOLD_REG",
    0x20002c4 : "TOP_DDOS_MAX_COUNT_REG",
    0x20002c8 : "TOP_DDOS_CONTROL_MODE_REG",
    0x20002cc : "TOP_DDOS_FLUSH_SIGNAL_REG",
    0x20002d0 : "TOP_DDOS_COUNT_1_REG",
    0x20002d4 : "TOP_DDOS_SRC_IP_1_REG",
    0x20002d8 : "TOP_DDOS_DETECTED_IP_REG",

    0x2000300 : "BRAM_OQ_DISABLE_QUEUES_REG",
    0x2000380 : "BRAM_OQ_QUEUE_0_NUM_PKT_BYTES_RECEIVED_REG",
    0x2000384 : "BRAM_OQ_QUEUE_0_NUM_PKTS_RECEIVED_REG",
    0x2000388 : "BRAM_OQ_QUEUE_0_NUM_PKTS_DROPPED_REG",
    0x200038c : "BRAM_OQ_QUEUE_0_NUM_WORDS_IN_QUEUE_REG",
    0x2000390 : "BRAM_OQ_QUEUE_1_NUM_PKT_BYTES_RECEIVED_REG",
    0x2000394 : "BRAM_OQ_QUEUE_1_NUM_PKTS_RECEIVED_REG",
    0x2000398 : "BRAM_OQ_QUEUE_1_NUM_PKTS_DROPPED_REG",
    0x200039c : "BRAM_OQ_QUEUE_1_NUM_WORDS_IN_QUEUE_REG",
    0x20003a0 : "BRAM_OQ_QUEUE_2_NUM_PKT_BYTES_RECEIVED_REG",
    0x20003a4 : "BRAM_OQ_QUEUE_2_NUM_PKTS_RECEIVED_REG",
    0x20003a8 : "BRAM_OQ_QUEUE_2_NUM_PKTS_DROPPED_REG",
    0x20003ac : "BRAM_OQ_QUEUE_2_NUM_WORDS_IN_QUEUE_REG",
    0x20003b0 : "BRAM_OQ_QUEUE_3_NUM_PKT_BYTES_RECEIVED_REG",
    0x20003b4 : "BRAM_OQ_QUEUE_3_NUM_PKTS_RECEIVED_REG",
    0x20003b8 : "BRAM_OQ_QUEUE_3_NUM_PKTS_DROPPED_REG",
    0x20003bc : "BRAM_OQ_QUEUE_3_NUM_WORDS_IN_QUEUE_REG",
    0x20003c0 : "BRAM_OQ_QUEUE_4_NUM_PKT_BYTES_RECEIVED_REG",
    0x20003c4 : "BRAM_OQ_QUEUE_4_NUM_PKTS_RECEIVED_REG",
    0x20003c8 : "BRAM_OQ_QUEUE_4_NUM_PKTS_DROPPED_REG",
    0x20003cc : "BRAM_OQ_QUEUE_4_NUM_WORDS_IN_QUEUE_REG",
    0x20003d0 : "BRAM_OQ_QUEUE_5_NUM_PKT_BYTES_RECEIVED_REG",
    0x20003d4 : "BRAM_OQ_QUEUE_5_NUM_PKTS_RECEIVED_REG",
    0x20003d8 : "BRAM_OQ_QUEUE_5_NUM_PKTS_DROPPED_REG",
    0x20003dc : "BRAM_OQ_QUEUE_5_NUM_WORDS_IN_QUEUE_REG",
    0x20003e0 : "BRAM_OQ_QUEUE_6_NUM_PKT_BYTES_RECEIVED_REG",
    0x20003e4 : "BRAM_OQ_QUEUE_6_NUM_PKTS_RECEIVED_REG",
    0x20003e8 : "BRAM_OQ_QUEUE_6_NUM_PKTS_DROPPED_REG",
    0x20003ec : "BRAM_OQ_QUEUE_6_NUM_WORDS_IN_QUEUE_REG",
    0x20003f0 : "BRAM_OQ_QUEUE_7_NUM_PKT_BYTES_RECEIVED_REG",
    0x20003f4 : "BRAM_OQ_QUEUE_7_NUM_PKTS_RECEIVED_REG",
    0x20003f8 : "BRAM_OQ_QUEUE_7_NUM_PKTS_DROPPED_REG",
    0x20003fc : "BRAM_OQ_QUEUE_7_NUM_WORDS_IN_QUEUE_REG",

    0x2000400 : "WDT_ENABLE_FLG_REG",
    0x2000404 : "WDT_COUNTER_REG",

    0x2001000 : "OPENFLOW_WILDCARD_LOOKUP_ACTION_0_REG",
    0x2001004 : "OPENFLOW_WILDCARD_LOOKUP_ACTION_1_REG",
    0x2001008 : "OPENFLOW_WILDCARD_LOOKUP_ACTION_2_REG",
    0x200100c : "OPENFLOW_WILDCARD_LOOKUP_ACTION_3_REG",
    0x2001010 : "OPENFLOW_WILDCARD_LOOKUP_ACTION_4_REG",
    0x2001014 : "OPENFLOW_WILDCARD_LOOKUP_ACTION_5_REG",
    0x2001018 : "OPENFLOW_WILDCARD_LOOKUP_ACTION_6_REG",
    0x200101c : "OPENFLOW_WILDCARD_LOOKUP_ACTION_7_REG",
    0x2001020 : "OPENFLOW_WILDCARD_LOOKUP_ACTION_8_REG",
    0x2001024 : "OPENFLOW_WILDCARD_LOOKUP_ACTION_9_REG",
    0x2001028 : "OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_0_REG",
    0x200102c : "OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_1_REG",
    0x2001030 : "OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_2_REG",
    0x2001034 : "OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_3_REG",
    0x2001038 : "OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_4_REG",
    0x200103c : "OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_5_REG",
    0x2001040 : "OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_6_REG",
    0x2001044 : "OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_7_REG",
    0x2001048 : "OPENFLOW_WILDCARD_LOOKUP_CMP_0_REG",
    0x200104c : "OPENFLOW_WILDCARD_LOOKUP_CMP_1_REG",
    0x2001050 : "OPENFLOW_WILDCARD_LOOKUP_CMP_2_REG",
    0x2001054 : "OPENFLOW_WILDCARD_LOOKUP_CMP_3_REG",
    0x2001058 : "OPENFLOW_WILDCARD_LOOKUP_CMP_4_REG",
    0x200105c : "OPENFLOW_WILDCARD_LOOKUP_CMP_5_REG",
    0x2001060 : "OPENFLOW_WILDCARD_LOOKUP_CMP_6_REG",
    0x2001064 : "OPENFLOW_WILDCARD_LOOKUP_CMP_7_REG",
    0x2001068 : "OPENFLOW_WILDCARD_LOOKUP_READ_ADDR_REG",
    0x200106c : "OPENFLOW_WILDCARD_LOOKUP_WRITE_ADDR_REG",
    0x2001070 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_0_REG",
    0x2001074 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_1_REG",
    0x2001078 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_2_REG",
    0x200107c : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_3_REG",
    0x2001080 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_4_REG",
    0x2001084 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_5_REG",
    0x2001088 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_6_REG",
    0x200108c : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_7_REG",
    0x2001090 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_8_REG",
    0x2001094 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_9_REG",
    0x2001098 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_10_REG",
    0x200109c : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_11_REG",
    0x20010a0 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_12_REG",
    0x20010a4 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_13_REG",
    0x20010a8 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_14_REG",
    0x20010ac : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_15_REG",
    0x20010b0 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_16_REG",
    0x20010b4 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_17_REG",
    0x20010b8 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_18_REG",
    0x20010bc : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_19_REG",
    0x20010c0 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_20_REG",
    0x20010c4 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_21_REG",
    0x20010c8 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_22_REG",
    0x20010cc : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_23_REG",
    0x20010d0 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_24_REG",
    0x20010d4 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_25_REG",
    0x20010d8 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_26_REG",
    0x20010dc : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_27_REG",
    0x20010e0 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_28_REG",
    0x20010e4 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_29_REG",
    0x20010e8 : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_30_REG",
    0x20010ec : "OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_31_REG",
    0x20010f0 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_0_REG",
    0x20010f4 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_1_REG",
    0x20010f8 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_2_REG",
    0x20010fc : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_3_REG",
    0x2001100 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_4_REG",
    0x2001104 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_5_REG",
    0x2001108 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_6_REG",
    0x200110c : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_7_REG",
    0x2001110 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_8_REG",
    0x2001114 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_9_REG",
    0x2001118 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_10_REG",
    0x200111c : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_11_REG",
    0x2001120 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_12_REG",
    0x2001124 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_13_REG",
    0x2001128 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_14_REG",
    0x200112c : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_15_REG",
    0x2001130 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_16_REG",
    0x2001134 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_17_REG",
    0x2001138 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_18_REG",
    0x200113c : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_19_REG",
    0x2001140 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_20_REG",
    0x2001144 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_21_REG",
    0x2001148 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_22_REG",
    0x200114c : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_23_REG",
    0x2001150 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_24_REG",
    0x2001154 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_25_REG",
    0x2001158 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_26_REG",
    0x200115c : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_27_REG",
    0x2001160 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_28_REG",
    0x2001164 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_29_REG",
    0x2001168 : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_30_REG",
    0x200116c : "OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_31_REG",
    0x2001170 : "OPENFLOW_WILDCARD_LOOKUP_DUMMY_1_REG",
    0x2001174 : "OPENFLOW_WILDCARD_LOOKUP_DUMMY_2_REG",
    0x2001178 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_0_REG",
    0x200117c : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_1_REG",
    0x2001180 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_2_REG",
    0x2001184 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_3_REG",
    0x2001188 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_4_REG",
    0x200118c : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_5_REG",
    0x2001190 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_6_REG",
    0x2001194 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_7_REG",
    0x2001198 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_8_REG",
    0x200119c : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_9_REG",
    0x20011a0 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_10_REG",
    0x20011a4 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_11_REG",
    0x20011a8 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_12_REG",
    0x20011ac : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_13_REG",
    0x20011b0 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_14_REG",
    0x20011b4 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_15_REG",
    0x20011b8 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_16_REG",
    0x20011bc : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_17_REG",
    0x20011c0 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_18_REG",
    0x20011c4 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_19_REG",
    0x20011c8 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_20_REG",
    0x20011cc : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_21_REG",
    0x20011d0 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_22_REG",
    0x20011d4 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_23_REG",
    0x20011d8 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_24_REG",
    0x20011dc : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_25_REG",
    0x20011e0 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_26_REG",
    0x20011e4 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_27_REG",
    0x20011e8 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_28_REG",
    0x20011ec : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_29_REG",
    0x20011f0 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_30_REG",
    0x20011f4 : "OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_31_REG",

})




# End of File
