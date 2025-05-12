from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.environ.get('TOKEN')
ADMIN_LIST = os.environ.get('ADMIN_LIST').split(',')


