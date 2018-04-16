///////////////////////////////////////////////////////////////////////////////
//
// Module: registers.v
// Project: OpenFlow Switch (openflow_switch)
// Description: Project specific register defines
//
//              OpenFlow Switch
//
///////////////////////////////////////////////////////////////////////////////

// -------------------------------------
//   Version Information
// -------------------------------------

`define DEVICE_ID          0
`define DEVICE_MAJOR       1
`define DEVICE_MINOR       0
`define DEVICE_REVISION    4
`define DEVICE_PROJ_DIR    "openflow_switch"
`define DEVICE_PROJ_NAME   "OpenFlow Switch"
`define DEVICE_PROJ_DESC   "OpenFlow Switch"


// -------------------------------------
//   Constants
// -------------------------------------

// ===== File: lib/verilog/core/common/xml/global.xml =====

// Maximum number of phy ports
`define MAX_PHY_PORTS                             4

// PCI address bus width
`define PCI_ADDR_WIDTH                            32

// PCI data bus width
`define PCI_DATA_WIDTH                            32

// PCI byte enable bus width
`define PCI_BE_WIDTH                              4

// CPCI--CNET address bus width. This is byte addresses even though bottom bits are zero.
`define CPCI_CNET_ADDR_WIDTH                      27

// CPCI--CNET data bus width
`define CPCI_CNET_DATA_WIDTH                      32

// CPCI--Virtex address bus width. This is byte addresses even though bottom bits are zero.
`define CPCI_NF2_ADDR_WIDTH                       27

// CPCI--Virtex data bus width
`define CPCI_NF2_DATA_WIDTH                       32

// DMA data bus width
`define DMA_DATA_WIDTH                            32

// DMA control bus width
`define DMA_CTRL_WIDTH                            4

// CPCI debug bus width
`define CPCI_DEBUG_DATA_WIDTH                     29

// SRAM address width
`define SRAM_ADDR_WIDTH                           19

// SRAM data width
`define SRAM_DATA_WIDTH                           36

// DRAM address width
`define DRAM_ADDR_WIDTH                           24


// ===== File: lib/verilog/core/common/xml/nf_defines.xml =====

// Clock period of 125 MHz clock in ns
`define FAST_CLK_PERIOD                           8

// Clock period of 62.5 MHz clock in ns
`define SLOW_CLK_PERIOD                           16

// Header value used by the IO queues
`define IO_QUEUE_STAGE_NUM                        8'hff

// Data path data width
`define DATA_WIDTH                                64

// Data path control width
`define CTRL_WIDTH                                8


// ===== File: projects/openflow_switch/include/output_port_lookup.xml =====

`define FAST_CLOCK_PERIOD                         8


// ===== File: projects/openflow_switch/include/vlan_remover.xml =====

`define VLAN_CTRL_WORD                            8'h42

`define VLAN_ETHERTYPE                            16'h8100


// ===== File: lib/verilog/core/output_queues/bram_output_queues/xml/bram_output_queues.xml =====

`define NUM_OUTPUT_QUEUES                         8


// ===== File: projects/openflow_switch/include/opl_processor.xml =====

`define NF2_OFPAT_OUTPUT                          16'h0001

`define NF2_OFPAT_SET_VLAN_VID                    16'h0002

`define NF2_OFPAT_SET_VLAN_PCP                    16'h0004

`define NF2_OFPAT_STRIP_VLAN                      16'h0008

`define NF2_OFPAT_SET_DL_SRC                      16'h0010

`define NF2_OFPAT_SET_DL_DST                      16'h0020

`define NF2_OFPAT_SET_NW_SRC                      16'h0040

`define NF2_OFPAT_SET_NW_DST                      16'h0080

`define NF2_OFPAT_SET_NW_TOS                      16'h0100

`define NF2_OFPAT_SET_TP_SRC                      16'h0200

`define NF2_OFPAT_SET_TP_DST                      16'h0400


// ===== File: projects/openflow_switch/include/wildcard_match.xml =====

`define OPENFLOW_WILDCARD_TABLE_SIZE              32

`define OPENFLOW_WILDCARD_NUM_DATA_WORDS_USED     10

`define OPENFLOW_WILDCARD_NUM_CMP_WORDS_USED      8


// ===== File: lib/verilog/core/utils/xml/device_id_reg.xml =====

// Total number of registers
`define DEV_ID_NUM_REGS                           64

// Number of non string registers
`define DEV_ID_NON_STR_REGS                       7

// Length of MD5 sum (bits)
`define DEV_ID_MD5SUM_LENGTH                      128

// Project directory length (in words, not chars)
`define DEV_ID_PROJ_DIR_WORD_LEN                  16

// Project directory length (in bytes/chars)
`define DEV_ID_PROJ_DIR_BYTE_LEN                  64

// Project directory length (in bits)
`define DEV_ID_PROJ_DIR_BIT_LEN                   512

// Project name length (in words, not chars)
`define DEV_ID_PROJ_NAME_WORD_LEN                 16

// Project name length (in bytes/chars)
`define DEV_ID_PROJ_NAME_BYTE_LEN                 64

// Project name length (in bits)
`define DEV_ID_PROJ_NAME_BIT_LEN                  512

// Device description length (in words, not chars)
`define DEV_ID_PROJ_DESC_WORD_LEN                 25

// Device description length (in bytes/chars)
`define DEV_ID_PROJ_DESC_BYTE_LEN                 100

// Device description length (in bits)
`define DEV_ID_PROJ_DESC_BIT_LEN                  800

// MD5 identifier (v1): MD5 sum of the string "device_id.v"
`define DEV_ID_MD5_VALUE_V1                       128'h4071736d8a603d2b4d55f62989a73c95
`define DEV_ID_MD5_VALUE_V1_0                     32'h4071736d
`define DEV_ID_MD5_VALUE_V1_1                     32'h8a603d2b
`define DEV_ID_MD5_VALUE_V1_2                     32'h4d55f629
`define DEV_ID_MD5_VALUE_V1_3                     32'h89a73c95

// MD5 identifier (v2): MD5 sum of the string "device_id.v:v2"
`define DEV_ID_MD5_VALUE_V2                       128'h5e461ffe439725c9279a22a1855f6c53
`define DEV_ID_MD5_VALUE_V2_0                     32'h5e461ffe
`define DEV_ID_MD5_VALUE_V2_1                     32'h439725c9
`define DEV_ID_MD5_VALUE_V2_2                     32'h279a22a1
`define DEV_ID_MD5_VALUE_V2_3                     32'h855f6c53

// Total number of registers (v1)
`define DEV_ID_NUM_REGS_V1                        64

// Number of non string registers (v1)
`define DEV_ID_NON_STR_REGS_V1                    7

// Project name length (v1: in words, not chars)
`define DEV_ID_PROJ_NAME_WORD_LEN_V1              25

// Project name length (v1: in bytes/chars)
`define DEV_ID_PROJ_NAME_BYTE_LEN_V1              100

// Project name length (v1: in bits)
`define DEV_ID_PROJ_NAME_BIT_LEN_V1               800


// ===== File: projects/openflow_switch/include/watchdog.xml =====

`define WDT_CPCI_REG_CTRL                         32'h00000008


// ===== File: projects/openflow_switch/include/header_parser.xml =====

`define ETH_TYPE_IP                               16'h0800

`define ETH_TYPE_ARP                              16'h0806

`define IP_PROTO_TCP                              8'h06

`define IP_PROTO_UDP                              8'h11

`define IP_PROTO_ICMP                             8'h01


// ===== File: lib/verilog/core/io_queues/cpu_dma_queue/xml/cpu_dma_queue.xml =====

`define CPU_QUEUE_REGS_ENABLE                     32'h00000000

`define CPU_QUEUE_REGS_DISABLE                    32'h00000001


// ===== File: lib/verilog/core/io_queues/ethernet_queue/xml/ethernet_mac.xml =====

// TX queue disable bit
`define MAC_GRP_TX_QUEUE_DISABLE_BIT_NUM          0

// RX queue disable bit
`define MAC_GRP_RX_QUEUE_DISABLE_BIT_NUM          1

// Reset MAC bit
`define MAC_GRP_RESET_MAC_BIT_NUM                 2

// MAC TX queue disable bit
`define MAC_GRP_MAC_DISABLE_TX_BIT_NUM            3

// MAC RX queue disable bit
`define MAC_GRP_MAC_DISABLE_RX_BIT_NUM            4

// MAC disable jumbo TX bit
`define MAC_GRP_MAC_DIS_JUMBO_TX_BIT_NUM          5

// MAC disable jumbo RX bit
`define MAC_GRP_MAC_DIS_JUMBO_RX_BIT_NUM          6

// MAC disable crc check disable bit
`define MAC_GRP_MAC_DIS_CRC_CHECK_BIT_NUM         7

// MAC disable crc generate bit
`define MAC_GRP_MAC_DIS_CRC_GEN_BIT_NUM           8


// ===== File: projects/openflow_switch/include/match_arbiter.xml =====

`define OPENFLOW_ENTRY_TRANSP_DST_WIDTH           16

`define OPENFLOW_ENTRY_TRANSP_DST_POS             0

`define OPENFLOW_ENTRY_TRANSP_SRC_WIDTH           16

`define OPENFLOW_ENTRY_TRANSP_SRC_POS             16

`define OPENFLOW_ENTRY_IP_PROTO_WIDTH             8

`define OPENFLOW_ENTRY_IP_PROTO_POS               32

`define OPENFLOW_ENTRY_IP_DST_WIDTH               32

`define OPENFLOW_ENTRY_IP_DST_POS                 40

`define OPENFLOW_ENTRY_IP_SRC_WIDTH               32

`define OPENFLOW_ENTRY_IP_SRC_POS                 72

`define OPENFLOW_ENTRY_ETH_TYPE_WIDTH             16

`define OPENFLOW_ENTRY_ETH_TYPE_POS               104

`define OPENFLOW_ENTRY_ETH_DST_WIDTH              48

`define OPENFLOW_ENTRY_ETH_DST_POS                120

`define OPENFLOW_ENTRY_ETH_SRC_WIDTH              48

`define OPENFLOW_ENTRY_ETH_SRC_POS                168

`define OPENFLOW_ENTRY_SRC_PORT_WIDTH             8

`define OPENFLOW_ENTRY_SRC_PORT_POS               216

`define OPENFLOW_ENTRY_IP_TOS_WIDTH               8

`define OPENFLOW_ENTRY_IP_TOS_POS                 224

`define OPENFLOW_ENTRY_VLAN_ID_WIDTH              16

`define OPENFLOW_ENTRY_VLAN_ID_POS                232

`define OPENFLOW_ENTRY_WIDTH                      248

// The actionfield is composed of a bitmask specifying actions to take and arguments.
`define OPENFLOW_ACTION_WIDTH                     320

// Ports to forward on
`define OPENFLOW_FORWARD_BITMASK_WIDTH            16

`define OPENFLOW_FORWARD_BITMASK_POS              0

`define OPENFLOW_NF2_ACTION_FLAG_WIDTH            16

`define OPENFLOW_NF2_ACTION_FLAG_POS              16

// Vlan ID to be replaced
`define OPENFLOW_SET_VLAN_VID_WIDTH               16

`define OPENFLOW_SET_VLAN_VID_POS                 32

// Vlan priority to be replaced
`define OPENFLOW_SET_VLAN_PCP_WIDTH               8

`define OPENFLOW_SET_VLAN_PCP_POS                 48

// Source MAC address to be replaced
`define OPENFLOW_SET_DL_SRC_WIDTH                 48

`define OPENFLOW_SET_DL_SRC_POS                   56

// Destination MAC address to be replaced
`define OPENFLOW_SET_DL_DST_WIDTH                 48

`define OPENFLOW_SET_DL_DST_POS                   104

// Source network address to be replaced
`define OPENFLOW_SET_NW_SRC_WIDTH                 32

`define OPENFLOW_SET_NW_SRC_POS                   152

// Destination network address to be replaced
`define OPENFLOW_SET_NW_DST_WIDTH                 32

`define OPENFLOW_SET_NW_DST_POS                   184

// TOS to be replaced
`define OPENFLOW_SET_NW_TOS_WIDTH                 8

`define OPENFLOW_SET_NW_TOS_POS                   216

// Source transport port to be replaced
`define OPENFLOW_SET_TP_SRC_WIDTH                 16

`define OPENFLOW_SET_TP_SRC_POS                   224

// Destination transport port to be replaced
`define OPENFLOW_SET_TP_DST_WIDTH                 16

`define OPENFLOW_SET_TP_DST_POS                   240


// ===== File: projects/openflow_switch/include/exact_match.xml =====

`define OPENFLOW_EXACT_ENTRY_PKT_COUNTER_WIDTH    25

`define OPENFLOW_EXACT_ENTRY_PKT_COUNTER_POS      0

`define OPENFLOW_EXACT_ENTRY_LAST_SEEN_WIDTH      7

`define OPENFLOW_EXACT_ENTRY_LAST_SEEN_POS        25

`define OPENFLOW_EXACT_ENTRY_BYTE_COUNTER_WIDTH   32

`define OPENFLOW_EXACT_ENTRY_BYTE_COUNTER_POS     32

`define OPENFLOW_EXACT_ENTRY_HDR_BASE_POS         32'h00000000

`define OPENFLOW_EXACT_ENTRY_COUNTERS_POS         32'h00000008

`define OPENFLOW_EXACT_ENTRY_ACTION_BASE_POS      32'h0000000a



// -------------------------------------
//   Modules
// -------------------------------------

// Tag/address widths
`define BRAM_OQ_BLOCK_ADDR_WIDTH                   17
`define BRAM_OQ_REG_ADDR_WIDTH                     6
`define CORE_BLOCK_ADDR_WIDTH                      1
`define CORE_REG_ADDR_WIDTH                        22
`define CPU_QUEUE_BLOCK_ADDR_WIDTH                 4
`define CPU_QUEUE_REG_ADDR_WIDTH                   16
`define DEV_ID_BLOCK_ADDR_WIDTH                    4
`define DEV_ID_REG_ADDR_WIDTH                      16
`define DMA_BLOCK_ADDR_WIDTH                       4
`define DMA_REG_ADDR_WIDTH                         16
`define DRAM_BLOCK_ADDR_WIDTH                      1
`define DRAM_REG_ADDR_WIDTH                        24
`define EXACT_MATCH_BLOCK_ADDR_WIDTH               19
`define EXACT_MATCH_REG_ADDR_WIDTH                 4
`define HEADER_PARSER_BLOCK_ADDR_WIDTH             19
`define HEADER_PARSER_REG_ADDR_WIDTH               4
`define IN_ARB_BLOCK_ADDR_WIDTH                    17
`define IN_ARB_REG_ADDR_WIDTH                      6
`define MAC_GRP_BLOCK_ADDR_WIDTH                   4
`define MAC_GRP_REG_ADDR_WIDTH                     16
`define MATCH_ARBITER_BLOCK_ADDR_WIDTH             19
`define MATCH_ARBITER_REG_ADDR_WIDTH               4
`define MDIO_BLOCK_ADDR_WIDTH                      4
`define MDIO_REG_ADDR_WIDTH                        16
`define OPENFLOW_LOOKUP_BLOCK_ADDR_WIDTH           17
`define OPENFLOW_LOOKUP_REG_ADDR_WIDTH             6
`define OPENFLOW_WILDCARD_LOOKUP_BLOCK_ADDR_WIDTH  13
`define OPENFLOW_WILDCARD_LOOKUP_REG_ADDR_WIDTH    10
`define OPL_PROCESSOR_BLOCK_ADDR_WIDTH             19
`define OPL_PROCESSOR_REG_ADDR_WIDTH               4
`define SRAM_BLOCK_ADDR_WIDTH                      1
`define SRAM_REG_ADDR_WIDTH                        22
`define TOP_DDOS_BLOCK_ADDR_WIDTH                  19
`define TOP_DDOS_REG_ADDR_WIDTH                    4
`define UDP_BLOCK_ADDR_WIDTH                       1
`define UDP_REG_ADDR_WIDTH                         23
`define VLAN_REMOVER_BLOCK_ADDR_WIDTH              19
`define VLAN_REMOVER_REG_ADDR_WIDTH                4
`define WDT_BLOCK_ADDR_WIDTH                       17
`define WDT_REG_ADDR_WIDTH                         6

// Module tags
`define CORE_BLOCK_ADDR                      1'h0
`define DEV_ID_BLOCK_ADDR                    4'h0
`define MDIO_BLOCK_ADDR                      4'h1
`define DMA_BLOCK_ADDR                       4'h4
`define MAC_GRP_0_BLOCK_ADDR                 4'h8
`define MAC_GRP_1_BLOCK_ADDR                 4'h9
`define MAC_GRP_2_BLOCK_ADDR                 4'ha
`define MAC_GRP_3_BLOCK_ADDR                 4'hb
`define CPU_QUEUE_0_BLOCK_ADDR               4'hc
`define CPU_QUEUE_1_BLOCK_ADDR               4'hd
`define CPU_QUEUE_2_BLOCK_ADDR               4'he
`define CPU_QUEUE_3_BLOCK_ADDR               4'hf
`define SRAM_BLOCK_ADDR                      1'h1
`define UDP_BLOCK_ADDR                       1'h1
`define OPENFLOW_LOOKUP_BLOCK_ADDR           17'h00000
`define IN_ARB_BLOCK_ADDR                    17'h00001
`define VLAN_REMOVER_BLOCK_ADDR              19'h00008
`define OPL_PROCESSOR_BLOCK_ADDR             19'h00009
`define HEADER_PARSER_BLOCK_ADDR             19'h0000a
`define TOP_DDOS_BLOCK_ADDR                  19'h0000b
`define BRAM_OQ_BLOCK_ADDR                   17'h00003
`define WDT_BLOCK_ADDR                       17'h00004
`define MATCH_ARBITER_BLOCK_ADDR             19'h00014
`define EXACT_MATCH_BLOCK_ADDR               19'h00015
`define OPENFLOW_WILDCARD_LOOKUP_BLOCK_ADDR  13'h0001
`define DRAM_BLOCK_ADDR                      1'h1


// -------------------------------------
//   Registers
// -------------------------------------

// Name: bram_output_queues
// Description: BRAM-based output queues
// File: lib/verilog/core/output_queues/bram_output_queues/xml/bram_output_queues.xml
//   Register group: QUEUE
//
//   Address decompositions:
//     - Inst:  Addresses of the *instances* within the module
//     - Group: Addresses of the *group* within the module
`define BRAM_OQ_QUEUE_GROUP_BLOCK_ADDR_WIDTH   1
`define BRAM_OQ_QUEUE_GROUP_REG_ADDR_WIDTH     5

`define BRAM_OQ_QUEUE_GROUP_BLOCK_ADDR         1'd1

`define BRAM_OQ_QUEUE_INST_BLOCK_ADDR_WIDTH    4
`define BRAM_OQ_QUEUE_INST_REG_ADDR_WIDTH      2

`define BRAM_OQ_QUEUE_0_INST_BLOCK_ADDR  4'd0
`define BRAM_OQ_QUEUE_1_INST_BLOCK_ADDR  4'd1
`define BRAM_OQ_QUEUE_2_INST_BLOCK_ADDR  4'd2
`define BRAM_OQ_QUEUE_3_INST_BLOCK_ADDR  4'd3
`define BRAM_OQ_QUEUE_4_INST_BLOCK_ADDR  4'd4
`define BRAM_OQ_QUEUE_5_INST_BLOCK_ADDR  4'd5
`define BRAM_OQ_QUEUE_6_INST_BLOCK_ADDR  4'd6
`define BRAM_OQ_QUEUE_7_INST_BLOCK_ADDR  4'd7

`define BRAM_OQ_QUEUE_NUM_PKT_BYTES_RECEIVED  2'h0
`define BRAM_OQ_QUEUE_NUM_PKTS_RECEIVED       2'h1
`define BRAM_OQ_QUEUE_NUM_PKTS_DROPPED        2'h2
`define BRAM_OQ_QUEUE_NUM_WORDS_IN_QUEUE      2'h3

`define BRAM_OQ_DISABLE_QUEUES  6'h0

// Name: cpu_dma_queue
// Description: CPU DMA queue
// File: lib/verilog/core/io_queues/cpu_dma_queue/xml/cpu_dma_queue.xml
`define CPU_QUEUE_CONTROL                        16'h0
`define CPU_QUEUE_RX_QUEUE_NUM_PKTS_IN_QUEUE     16'h1
`define CPU_QUEUE_RX_QUEUE_NUM_PKTS_ENQUEUED     16'h2
`define CPU_QUEUE_RX_QUEUE_NUM_PKTS_DROPPED_BAD  16'h3
`define CPU_QUEUE_RX_QUEUE_NUM_PKTS_DEQUEUED     16'h4
`define CPU_QUEUE_RX_QUEUE_NUM_UNDERRUNS         16'h5
`define CPU_QUEUE_RX_QUEUE_NUM_OVERRUNS          16'h6
`define CPU_QUEUE_RX_QUEUE_NUM_WORDS_PUSHED      16'h7
`define CPU_QUEUE_RX_QUEUE_NUM_BYTES_PUSHED      16'h8
`define CPU_QUEUE_TX_QUEUE_NUM_PKTS_IN_QUEUE     16'h9
`define CPU_QUEUE_TX_QUEUE_NUM_PKTS_ENQUEUED     16'ha
`define CPU_QUEUE_TX_QUEUE_NUM_PKTS_DEQUEUED     16'hb
`define CPU_QUEUE_TX_QUEUE_NUM_UNDERRUNS         16'hc
`define CPU_QUEUE_TX_QUEUE_NUM_OVERRUNS          16'hd
`define CPU_QUEUE_TX_QUEUE_NUM_WORDS_PUSHED      16'he
`define CPU_QUEUE_TX_QUEUE_NUM_BYTES_PUSHED      16'hf

// Name: device_id
// Description: Device identification
// File: lib/verilog/core/utils/xml/device_id_reg.xml
`define DEV_ID_MD5_0         16'h0
`define DEV_ID_MD5_1         16'h1
`define DEV_ID_MD5_2         16'h2
`define DEV_ID_MD5_3         16'h3
`define DEV_ID_DEVICE_ID     16'h4
`define DEV_ID_VERSION       16'h5
`define DEV_ID_CPCI_ID       16'h6
`define DEV_ID_PROJ_DIR_0    16'h7
`define DEV_ID_PROJ_DIR_1    16'h8
`define DEV_ID_PROJ_DIR_2    16'h9
`define DEV_ID_PROJ_DIR_3    16'ha
`define DEV_ID_PROJ_DIR_4    16'hb
`define DEV_ID_PROJ_DIR_5    16'hc
`define DEV_ID_PROJ_DIR_6    16'hd
`define DEV_ID_PROJ_DIR_7    16'he
`define DEV_ID_PROJ_DIR_8    16'hf
`define DEV_ID_PROJ_DIR_9    16'h10
`define DEV_ID_PROJ_DIR_10   16'h11
`define DEV_ID_PROJ_DIR_11   16'h12
`define DEV_ID_PROJ_DIR_12   16'h13
`define DEV_ID_PROJ_DIR_13   16'h14
`define DEV_ID_PROJ_DIR_14   16'h15
`define DEV_ID_PROJ_DIR_15   16'h16
`define DEV_ID_PROJ_NAME_0   16'h17
`define DEV_ID_PROJ_NAME_1   16'h18
`define DEV_ID_PROJ_NAME_2   16'h19
`define DEV_ID_PROJ_NAME_3   16'h1a
`define DEV_ID_PROJ_NAME_4   16'h1b
`define DEV_ID_PROJ_NAME_5   16'h1c
`define DEV_ID_PROJ_NAME_6   16'h1d
`define DEV_ID_PROJ_NAME_7   16'h1e
`define DEV_ID_PROJ_NAME_8   16'h1f
`define DEV_ID_PROJ_NAME_9   16'h20
`define DEV_ID_PROJ_NAME_10  16'h21
`define DEV_ID_PROJ_NAME_11  16'h22
`define DEV_ID_PROJ_NAME_12  16'h23
`define DEV_ID_PROJ_NAME_13  16'h24
`define DEV_ID_PROJ_NAME_14  16'h25
`define DEV_ID_PROJ_NAME_15  16'h26
`define DEV_ID_PROJ_DESC_0   16'h27
`define DEV_ID_PROJ_DESC_1   16'h28
`define DEV_ID_PROJ_DESC_2   16'h29
`define DEV_ID_PROJ_DESC_3   16'h2a
`define DEV_ID_PROJ_DESC_4   16'h2b
`define DEV_ID_PROJ_DESC_5   16'h2c
`define DEV_ID_PROJ_DESC_6   16'h2d
`define DEV_ID_PROJ_DESC_7   16'h2e
`define DEV_ID_PROJ_DESC_8   16'h2f
`define DEV_ID_PROJ_DESC_9   16'h30
`define DEV_ID_PROJ_DESC_10  16'h31
`define DEV_ID_PROJ_DESC_11  16'h32
`define DEV_ID_PROJ_DESC_12  16'h33
`define DEV_ID_PROJ_DESC_13  16'h34
`define DEV_ID_PROJ_DESC_14  16'h35
`define DEV_ID_PROJ_DESC_15  16'h36
`define DEV_ID_PROJ_DESC_16  16'h37
`define DEV_ID_PROJ_DESC_17  16'h38
`define DEV_ID_PROJ_DESC_18  16'h39
`define DEV_ID_PROJ_DESC_19  16'h3a
`define DEV_ID_PROJ_DESC_20  16'h3b
`define DEV_ID_PROJ_DESC_21  16'h3c
`define DEV_ID_PROJ_DESC_22  16'h3d
`define DEV_ID_PROJ_DESC_23  16'h3e
`define DEV_ID_PROJ_DESC_24  16'h3f

// Name: dma
// Description: DMA transfer module
// File: lib/verilog/core/dma/xml/dma.xml
`define DMA_CTRL               16'h0
`define DMA_NUM_INGRESS_PKTS   16'h1
`define DMA_NUM_INGRESS_BYTES  16'h2
`define DMA_NUM_EGRESS_PKTS    16'h3
`define DMA_NUM_EGRESS_BYTES   16'h4
`define DMA_NUM_TIMEOUTS       16'h5

// Name: exact_match
// Description: exact match lookup
// File: projects/openflow_switch/include/exact_match.xml

// Name: header_parser
// Description: Chop ether/IP/UDP-TCP header into 11 tuples
// File: projects/openflow_switch/include/header_parser.xml

// Name: in_arb
// Description: Round-robin input arbiter
// File: lib/verilog/core/input_arbiter/rr_input_arbiter/xml/rr_input_arbiter.xml
`define IN_ARB_NUM_PKTS_SENT       6'h0
`define IN_ARB_LAST_PKT_WORD_0_HI  6'h1
`define IN_ARB_LAST_PKT_WORD_0_LO  6'h2
`define IN_ARB_LAST_PKT_CTRL_0     6'h3
`define IN_ARB_LAST_PKT_WORD_1_HI  6'h4
`define IN_ARB_LAST_PKT_WORD_1_LO  6'h5
`define IN_ARB_LAST_PKT_CTRL_1     6'h6
`define IN_ARB_STATE               6'h7

// Name: match_arbiter
// Description: Arbitration between exact and wildcard lookups results
// File: projects/openflow_switch/include/match_arbiter.xml

// Name: mdio
// Description: MDIO interface
// File: lib/verilog/core/io/mdio/xml/mdio.xml
//   Register group: PHY
//
//   Address decompositions:
//     - Inst:  Addresses of the *instances* within the module
`define MDIO_PHY_INST_BLOCK_ADDR_WIDTH    11
`define MDIO_PHY_INST_REG_ADDR_WIDTH      5

`define MDIO_PHY_0_INST_BLOCK_ADDR  11'd0
`define MDIO_PHY_1_INST_BLOCK_ADDR  11'd1
`define MDIO_PHY_2_INST_BLOCK_ADDR  11'd2
`define MDIO_PHY_3_INST_BLOCK_ADDR  11'd3

`define MDIO_PHY_CONTROL                                 5'h0
`define MDIO_PHY_STATUS                                  5'h1
`define MDIO_PHY_PHY_ID_HI                               5'h2
`define MDIO_PHY_PHY_ID_LO                               5'h3
`define MDIO_PHY_AUTONEGOTIATION_ADVERT                  5'h4
`define MDIO_PHY_AUTONEG_LINK_PARTNER_BASE_PAGE_ABILITY  5'h5
`define MDIO_PHY_AUTONEG_EXPANSION                       5'h6
`define MDIO_PHY_AUTONEG_NEXT_PAGE_TX                    5'h7
`define MDIO_PHY_AUTONEG_LINK_PARTNER_RCVD_NEXT_PAGE     5'h8
`define MDIO_PHY_MASTER_SLAVE_CTRL                       5'h9
`define MDIO_PHY_MASTER_SLAVE_STATUS                     5'ha
`define MDIO_PHY_PSE_CTRL                                5'hb
`define MDIO_PHY_PSE_STATUS                              5'hc
`define MDIO_PHY_MMD_ACCESS_CTRL                         5'hd
`define MDIO_PHY_MMD_ACCESS_STATUS                       5'he
`define MDIO_PHY_EXTENDED_STATUS                         5'hf
`define MDIO_PHY_PHY_EXTENDED_CTRL                       5'h10
`define MDIO_PHY_PHY_EXTENDED_STATUS                     5'h11
`define MDIO_PHY_RX_ERROR_COUNT                          5'h12
`define MDIO_PHY_FALSE_CARRIER_SENSE_COUNT               5'h13
`define MDIO_PHY_RX_NOT_OK_COUNT                         5'h14
`define MDIO_PHY_EXPANSION_1                             5'h15
`define MDIO_PHY_EXPANSION_2                             5'h16
`define MDIO_PHY_EXPANSION_REG_ACCESS                    5'h17
`define MDIO_PHY_SHADOW_18                               5'h18
`define MDIO_PHY_AUX_STATUS                              5'h19
`define MDIO_PHY_INT_STATUS                              5'h1a
`define MDIO_PHY_INT_MASK                                5'h1b
`define MDIO_PHY_SHADOW_1C                               5'h1c
`define MDIO_PHY_SHADOW_1D                               5'h1d
`define MDIO_PHY_TEST                                    5'h1e
`define MDIO_PHY_RESERVED                                5'h1f


// Name: nf2_mac_grp
// Description: Ethernet MAC group
// File: lib/verilog/core/io_queues/ethernet_queue/xml/ethernet_mac.xml
`define MAC_GRP_CONTROL                         16'h0
`define MAC_GRP_RX_QUEUE_NUM_PKTS_IN_QUEUE      16'h1
`define MAC_GRP_RX_QUEUE_NUM_PKTS_STORED        16'h2
`define MAC_GRP_RX_QUEUE_NUM_PKTS_DROPPED_FULL  16'h3
`define MAC_GRP_RX_QUEUE_NUM_PKTS_DROPPED_BAD   16'h4
`define MAC_GRP_RX_QUEUE_NUM_PKTS_DEQUEUED      16'h5
`define MAC_GRP_RX_QUEUE_NUM_WORDS_PUSHED       16'h6
`define MAC_GRP_RX_QUEUE_NUM_BYTES_PUSHED       16'h7
`define MAC_GRP_TX_QUEUE_NUM_PKTS_IN_QUEUE      16'h8
`define MAC_GRP_TX_QUEUE_NUM_PKTS_ENQUEUED      16'h9
`define MAC_GRP_TX_QUEUE_NUM_PKTS_SENT          16'ha
`define MAC_GRP_TX_QUEUE_NUM_WORDS_PUSHED       16'hb
`define MAC_GRP_TX_QUEUE_NUM_BYTES_PUSHED       16'hc

// Name: openflow_output_port_lookup
// Description: Output Port Lookup for OpenFlow hardware datapath
// File: projects/openflow_switch/include/output_port_lookup.xml
`define OPENFLOW_LOOKUP_WILDCARD_MISSES     6'h0
`define OPENFLOW_LOOKUP_WILDCARD_HITS       6'h1
`define OPENFLOW_LOOKUP_EXACT_MISSES        6'h2
`define OPENFLOW_LOOKUP_EXACT_HITS          6'h3
`define OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_0  6'h4
`define OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_1  6'h5
`define OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_2  6'h6
`define OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_3  6'h7
`define OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_4  6'h8
`define OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_5  6'h9
`define OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_6  6'ha
`define OPENFLOW_LOOKUP_NUM_PKTS_DROPPED_7  6'hb
`define OPENFLOW_LOOKUP_DUMY_SOFTWARE_0     6'hc
`define OPENFLOW_LOOKUP_DUMY_SOFTWARE_1     6'hd
`define OPENFLOW_LOOKUP_TIMER               6'he

// Name: opl_processor
// Description: opl_processor
// File: projects/openflow_switch/include/opl_processor.xml

// Name: top_ddos
// Description: Registers for Clock controller Module
// File: projects/openflow_switch/include/top_ddos.xml
`define TOP_DDOS_THRESHOLD     4'h0
`define TOP_DDOS_MAX_COUNT     4'h1
`define TOP_DDOS_CONTROL_MODE  4'h2
`define TOP_DDOS_FLUSH_SIGNAL  4'h3
`define TOP_DDOS_COUNT_1       4'h4
`define TOP_DDOS_SRC_IP_1      4'h5
`define TOP_DDOS_DETECTED_IP   4'h6

// Name: vlan_remover
// Description: Remove vlan tag and ethtype if ethtype is vlan, and store them into module header
// File: projects/openflow_switch/include/vlan_remover.xml

// Name: watchdog
// Description: Watchdog timer
// File: projects/openflow_switch/include/watchdog.xml
`define WDT_ENABLE_FLG  6'h0
`define WDT_COUNTER     6'h1

// Name: wildcard_match
// Description: wildcard match lookup
// File: projects/openflow_switch/include/wildcard_match.xml
`define OPENFLOW_WILDCARD_LOOKUP_ACTION_0         10'h0
`define OPENFLOW_WILDCARD_LOOKUP_ACTION_1         10'h1
`define OPENFLOW_WILDCARD_LOOKUP_ACTION_2         10'h2
`define OPENFLOW_WILDCARD_LOOKUP_ACTION_3         10'h3
`define OPENFLOW_WILDCARD_LOOKUP_ACTION_4         10'h4
`define OPENFLOW_WILDCARD_LOOKUP_ACTION_5         10'h5
`define OPENFLOW_WILDCARD_LOOKUP_ACTION_6         10'h6
`define OPENFLOW_WILDCARD_LOOKUP_ACTION_7         10'h7
`define OPENFLOW_WILDCARD_LOOKUP_ACTION_8         10'h8
`define OPENFLOW_WILDCARD_LOOKUP_ACTION_9         10'h9
`define OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_0       10'ha
`define OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_1       10'hb
`define OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_2       10'hc
`define OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_3       10'hd
`define OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_4       10'he
`define OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_5       10'hf
`define OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_6       10'h10
`define OPENFLOW_WILDCARD_LOOKUP_CMP_MASK_7       10'h11
`define OPENFLOW_WILDCARD_LOOKUP_CMP_0            10'h12
`define OPENFLOW_WILDCARD_LOOKUP_CMP_1            10'h13
`define OPENFLOW_WILDCARD_LOOKUP_CMP_2            10'h14
`define OPENFLOW_WILDCARD_LOOKUP_CMP_3            10'h15
`define OPENFLOW_WILDCARD_LOOKUP_CMP_4            10'h16
`define OPENFLOW_WILDCARD_LOOKUP_CMP_5            10'h17
`define OPENFLOW_WILDCARD_LOOKUP_CMP_6            10'h18
`define OPENFLOW_WILDCARD_LOOKUP_CMP_7            10'h19
`define OPENFLOW_WILDCARD_LOOKUP_READ_ADDR        10'h1a
`define OPENFLOW_WILDCARD_LOOKUP_WRITE_ADDR       10'h1b
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_0      10'h1c
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_1      10'h1d
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_2      10'h1e
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_3      10'h1f
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_4      10'h20
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_5      10'h21
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_6      10'h22
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_7      10'h23
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_8      10'h24
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_9      10'h25
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_10     10'h26
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_11     10'h27
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_12     10'h28
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_13     10'h29
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_14     10'h2a
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_15     10'h2b
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_16     10'h2c
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_17     10'h2d
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_18     10'h2e
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_19     10'h2f
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_20     10'h30
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_21     10'h31
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_22     10'h32
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_23     10'h33
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_24     10'h34
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_25     10'h35
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_26     10'h36
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_27     10'h37
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_28     10'h38
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_29     10'h39
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_30     10'h3a
`define OPENFLOW_WILDCARD_LOOKUP_BYTES_HIT_31     10'h3b
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_0       10'h3c
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_1       10'h3d
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_2       10'h3e
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_3       10'h3f
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_4       10'h40
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_5       10'h41
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_6       10'h42
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_7       10'h43
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_8       10'h44
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_9       10'h45
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_10      10'h46
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_11      10'h47
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_12      10'h48
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_13      10'h49
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_14      10'h4a
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_15      10'h4b
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_16      10'h4c
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_17      10'h4d
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_18      10'h4e
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_19      10'h4f
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_20      10'h50
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_21      10'h51
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_22      10'h52
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_23      10'h53
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_24      10'h54
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_25      10'h55
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_26      10'h56
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_27      10'h57
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_28      10'h58
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_29      10'h59
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_30      10'h5a
`define OPENFLOW_WILDCARD_LOOKUP_PKTS_HIT_31      10'h5b
`define OPENFLOW_WILDCARD_LOOKUP_DUMMY_1          10'h5c
`define OPENFLOW_WILDCARD_LOOKUP_DUMMY_2          10'h5d
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_0   10'h5e
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_1   10'h5f
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_2   10'h60
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_3   10'h61
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_4   10'h62
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_5   10'h63
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_6   10'h64
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_7   10'h65
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_8   10'h66
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_9   10'h67
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_10  10'h68
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_11  10'h69
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_12  10'h6a
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_13  10'h6b
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_14  10'h6c
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_15  10'h6d
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_16  10'h6e
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_17  10'h6f
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_18  10'h70
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_19  10'h71
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_20  10'h72
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_21  10'h73
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_22  10'h74
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_23  10'h75
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_24  10'h76
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_25  10'h77
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_26  10'h78
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_27  10'h79
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_28  10'h7a
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_29  10'h7b
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_30  10'h7c
`define OPENFLOW_WILDCARD_LOOKUP_LAST_SEEN_TS_31  10'h7d



// -------------------------------------
//   Bitmasks
// -------------------------------------

// Type: dma_iface_ctrl
// Description: DMA interface control register
// File: lib/verilog/core/dma/xml/dma.xml
`define DMA_IFACE_CTRL_DISABLE_POS   0
`define DMA_IFACE_CTRL_RESET_POS     1

// Type: mii_ctrl
// Description: MII control register
// File: lib/verilog/core/io/mdio/xml/mdio.xml
`define MII_CTRL_RESET_POS               15
`define MII_CTRL_INTERNAL_LOOPBACK_POS   14
`define MII_CTRL_SPEED_SEL_LO_POS        13
`define MII_CTRL_AUTONEG_ENABLE_POS      12
`define MII_CTRL_PWR_DOWN_POS            11
`define MII_CTRL_ISOLATE_POS             10
`define MII_CTRL_RESTART_AUTONEG_POS     9
`define MII_CTRL_DUPLEX_MODE_POS         8
`define MII_CTRL_COLLISION_TEST_EN_POS   7
`define MII_CTRL_SPEED_SEL_HI_POS        6

// Type: mii_status
// Description: MII status register
// File: lib/verilog/core/io/mdio/xml/mdio.xml
`define MII_STATUS_100BASE_T4_CAPABLE_POS            15
`define MII_STATUS_100BASE_X_FULL_DPLX_CAPABLE_POS   14
`define MII_STATUS_100BASE_X_HALF_DPLX_CAPABLE_POS   13
`define MII_STATUS_10BASE_T_FULL_DPLX_CAPABLE_POS    12
`define MII_STATUS_10BASE_T_HALF_DPLX_CAPABLE_POS    11
`define MII_STATUS_10BASE_T2_FULL_DPLX_CAPABLE_POS   10
`define MII_STATUS_10BASE_T2_HALF_DPLX_CAPABLE_POS   9
`define MII_STATUS_EXTENDED_STATUS_POS               8
`define MII_STATUS_MF_PREAMBLE_SUPPRESS_POS          6
`define MII_STATUS_AUTONEG_COMPLETE_POS              5
`define MII_STATUS_REMOTE_FAULT_POS                  4
`define MII_STATUS_AUTONEG_ABILITY_POS               3
`define MII_STATUS_LINK_STATUS_POS                   2
`define MII_STATUS_JABBER_DETECT_POS                 1
`define MII_STATUS_EXTENDED_CAPABILITY_POS           0

// Type: cpu_queue_control
// Description: DMA queue control register
// File: lib/verilog/core/io_queues/cpu_dma_queue/xml/cpu_dma_queue.xml
`define CPU_QUEUE_CONTROL_TX_QUEUE_DISABLE_POS   0
`define CPU_QUEUE_CONTROL_RX_QUEUE_DISABLE_POS   1

// Type: mac_grp_control
// Description: MAC group control register
// File: lib/verilog/core/io_queues/ethernet_queue/xml/ethernet_mac.xml
`define MAC_GRP_CONTROL_TX_QUEUE_DISABLE_POS        0
`define MAC_GRP_CONTROL_RX_QUEUE_DISABLE_POS        1
`define MAC_GRP_CONTROL_RESET_MAC_POS               2
`define MAC_GRP_CONTROL_MAC_DISABLE_TX_POS          3
`define MAC_GRP_CONTROL_MAC_DISABLE_RX_POS          4
`define MAC_GRP_CONTROL_MAC_DISABLE_JUMBO_TX_POS    5
`define MAC_GRP_CONTROL_MAC_DISABLE_JUMBO_RX_POS    6
`define MAC_GRP_CONTROL_MAC_DISABLE_CRC_CHECK_POS   7
`define MAC_GRP_CONTROL_MAC_DISABLE_CRC_GEN_POS     8



