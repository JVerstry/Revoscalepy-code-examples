# settings.py
import os, sys, logging
from dotenv import load_dotenv
from pathlib import Path

# Do we have an .env file?
dir_path = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(dir_path, '.env')

if not os.path.isfile(env_path):
    logging.error('Missing .env file, copy .env_tmpl to .env')
    sys.exit()
    
# Loading .env file
load_dotenv()

DATA_LOCATION = os.environ.get("DATA_LOCATION")
