from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

medsync = Flask(__name__)


password = os.getenv("MONGO_PASSWORD")
db_name = os.getenv("MONGO_DB")

uri =f'mongodb+srv://nelysemathieu:{password}@cluster0.jtgg39q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = MongoClient(uri, server_api=ServerApi('1'))
db = client[f'{db_name}']


##test connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


from app.api_routes.get import api
from app.api_routes.post import post_routes
medsync.register_blueprint(api)
medsync.register_blueprint(post_routes)


