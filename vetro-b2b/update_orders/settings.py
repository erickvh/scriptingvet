# settings.py
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent.parent.absolute() / '.env'
load_dotenv(dotenv_path=env_path)

db_name = os.getenv('DB_NAME')  # db test
# db_name = os.getenv('DB_MASTER')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_driver = os.getenv('DB_DRIVER')
# there are required to access to api
api_key = os.getenv('API_KEY')
api_token = os.getenv('API_TOKEN')
carnet_id = os.getenv('CARNET')

# SMTP env
smtp_server = os.getenv('SMTP')
smtp_user = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASSWORD')
smtp_port = int(os.getenv('SMTP_PORT'))
first_destinatary = os.getenv('DESTINARY_ONE')
