# HTTP Request command
INIT_DESTROY = "0"
INIT_GEO = "1"
INIT_DATA = "2"

#HTTP Request
METHOD = "method"
TIMESTEP = "iter"
MODULE = "module"
MODULE_ID = "module_id"
MODULE_NUM = "module_num"
MODULE_TICK = "module_tick"
RESOURCES_NAME = "resources_name"
RESOURCES_METHOD = "resources_method"

CONTROL_URL = "control_url"
REDIS_URL_HTTP = "redis_url"
REDIS_PORT_HTTP = "redis_port"
REDIS_PASSWORD_HTTP = "redis_password"

INITIALIZE = '0'
RUN = '1'
TERMINATE = '2'
CHECK = '3'
ACQUIRE = '4'
RELEASE = '5'
RESUME = '6'

#Check timestep and signal
NEXT_STEP = 0
CURRENT_STEP = 1
TERMINATE_STEP = 2

# tissue number
AIR = 0
BLOOD = 1
REGULAR_TISSUE = 2
EPITHELIUM = 3
MMLAYER = 4 
PORES = 5 # macrophage movement layer

BLOOD_VESSEL_LAYER = 1

# construct code
CONSTRUCT_BASIC = 0
CONSTRUCT_EPI = 1
CONSTRUCT_VESSEL = 2

# process state
PROCESSING = 0
READY = 1

#Geometry 
QUADRIC = "quadric"
VECTOR = "vector"
PLANE = "plane"

#files path
SHARE = "share"
COMMON = "common"

# afumigatus tables
AFUMIGATUS_BYTESIZE = 98
AFUMIGATUS_SPECIES_NUM = 23
AFUMIGATUS_ITERATION = "iteration";
AFUMIGATUS_X = "x";
AFUMIGATUS_Y = "y";
AFUMIGATUS_Z = "z";
AFUMIGATUS_DX = "dx";
AFUMIGATUS_DY = "dy";
AFUMIGATUS_DZ = "dz";

AFUMIGATUS = "afumigatus"
AFUMIGATUS_BRANCHABLE = "branchable";
AFUMIGATUS_GROWABLE = "growable";
AFUMIGATUS_HEALTH = "health";
AFUMIGATUS_STATE = "state";
AFUMIGATUS_STATUS = "status";
AFUMIGATUS_IRON = "Iron";
AFUMIGATUS_GROWTH_TIME_LEFT = "growthTimeLeft";
AFUMIGATUS_BN = "BN";
AFUMIGATUS_ID = "_id";

# macrophage tables
MACROPHAGE_BYTESIZE = 64
MACROPHAGE_SPECIES_NUM = 13
MACROPHAGE = "macrophages"

MACRO_ITERATION = "macroIteration";
MACRO_STATE = "macroState";
MACRO_BN = "macroBN";
MACRO_HEALTH = "macroHealth";
MACRO_ATTACHED_FUNGUS = "macroAttachedFungus";
MACRO_COORDINATES = "macroCoordinate";
MACRO_SWALLOW_TIME_LEFT = "macroSwallowTimeLeft";
MACRO_IRON = "macroIron";

# molecules
IRON = "iron"
TAFC = "tafc"
TAFC_BI = "tafcbi"
APO_TRANSFERRIN = "apoTf"
TRANSFERRIN_BI = "TfBI"
CHEMOKINE = "macroCytokine"
