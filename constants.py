
KOTI_NRF_ADDR_CTRL = 0x00
KOTI_NRF_ADDR_BROADCAST = 0xff

KOTI_TYPE_ID_QUERY = 1
KOTI_TYPE_PSU = 2
KOTI_TYPE_WATER_FLOW_LITRE = 3
KOTI_TYPE_WATER_FLOW_MILLILITRE = 4
KOTI_TYPE_TH = 5
KOTI_TYPE_CLICK = 6
KOTI_TYPE_COUNT = 7
KOTI_TYPE_DEBUG = 255

KOTI_PSU_UNKNOWN = 0
KOTI_PSU_MAINS_GENERIC = 1
KOTI_PSU_BATTERY_LITHIUM = 0x41
KOTI_PSU_BATTERY_ALKALINE = 0x42
KOTI_PSU_BATTERY_RECHARGEABLE_LEAD = 0x81
KOTI_PSU_BATTERY_RECHARGEABLE_NICD = 0x82
KOTI_PSU_BATTERY_RECHARGEABLE_NIMH = 0x83

KOTI_NRF_PCK_HDR_SRC = 0
KOTI_NRF_PCK_HDR_DST = 1
KOTI_NRF_PCK_HDR_FLAGS = 2
KOTI_NRF_PCK_HDR_SEQ = 3
KOTI_NRF_PCK_HDR_CRC = 4
KOTI_NRF_PCK_HDR_TYPE = 6

KOTI_NRF_FLAG_ENC_BLOCKS_MASK = 0xe0
KOTI_NRF_FLAG_ENC_NONE = 0x00
KOTI_NRF_FLAG_ENC_RC5_1_BLOCK = 0x20
KOTI_NRF_FLAG_ENC_RC5_2_BLOCKS = 0x40
KOTI_NRF_FLAG_ENC_RC5_3_BLOCKS = 0x60
KOTI_NRF_FLAG_ENC_RC5_4_BLOCKS = 0x80
