# settings.py
import os, sys, logging
from dotenv import load_dotenv
from revoscalepy import RxOptions

# Logging & level

logger = logging.getLogger("Revoscalepy-code-examples")
# logger.setLevel(logging.INFO)

# Do we have an .env file?
dir_path = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(dir_path, '.env')

if not os.path.isfile(env_path):
    logging.error('Missing .env file, copy .env_tmpl to .env')
    sys.exit()
    
# Loading .env file
load_dotenv(env_path)

DATA_LOCATION = os.environ.get("DATA_LOCATION")
RESULTS_LOCATION = os.environ.get("RESULTS_LOCATION")
COMPRESSION_LEVEL = os.environ.get("COMPRESSION_LEVEL")

# Basic configuration

if not os.path.isdir(DATA_LOCATION):
    logging.error('Data directory not found: ' + DATA_LOCATION)
    sys.exit()

if os.path.isdir(RESULTS_LOCATION):
    RxOptions.set_option("OutDataPath", [RESULTS_LOCATION])
else:
    logging.error('Result directory not found: ' + RESULTS_LOCATION)
    sys.exit()

SAMPLE_DATA_DIR = RxOptions.get_option("sampleDataDir")

# 2.1 Data Compression in .xdf Files

RxOptions.set_option("XdfCompressionLevel", int(COMPRESSION_LEVEL))

