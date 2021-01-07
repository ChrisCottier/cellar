import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = f'mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.p7vht.mongodb.net/{DB_NAME}?retryWrites=true&w=majority'