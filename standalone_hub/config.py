from config_studio_hub import *

base_dir = '/Users/zcqian/Developer/biothings-devel/data/standalone'
DATA_ARCHIVE_ROOT = f'{base_dir}/data_archive'
DATA_PLUGIN_FOLDER = f'{base_dir}/plugin'
DATA_UPLOAD_FOLDER = f'{base_dir}/data_upload'
DATA_SRC_SERVER = 'localhost'
DATA_SRC_PORT = 27017
DATA_SRC_DATABASE = 'biothings_src'
DATA_SRC_SERVER_USERNAME = ''
DATA_SRC_SERVER_PASSWORD = ''

DATA_TARGET_SERVER = 'localhost'
DATA_TARGET_PORT = 27017
DATA_TARGET_DATABASE = 'biothings'
DATA_TARGET_SERVER_USERNAME = ''
DATA_TARGET_SERVER_PASSWORD = ''

DATA_HUB_DB_DATABASE = DATA_SRC_DATABASE # keep _src db as before

DIFF_PATH = f'{base_dir}/diff'

HUB_DB_BACKEND = {
		"module" : "biothings.utils.mongo",
		"uri" : "mongodb://localhost:27017",
		}

LOG_FOLDER = f'{base_dir}/logs'
logger = setup_default_log("hub", LOG_FOLDER)

RELEASE_PATH = f'{base_dir}/release'
CACHE_FOLDER = f'{base_dir}/cache'

RUN_DIR = f'{base_dir}/run'
CONFIG_READONLY = False

USE_RELOADER = False