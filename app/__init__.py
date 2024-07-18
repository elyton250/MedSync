from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_login import LoginManager
from flask_cors import CORS


login_manager = LoginManager()
load_dotenv()

medsync = Flask(__name__)

medsync.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

login_manager.init_app(medsync)


CORS(medsync)

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

@login_manager.user_loader
def load_user(user_id):
    return db.doctors.find_one({"_id": user_id})

from app.api_routes.get import api
from app.api_routes.post import post_routes
from app.api_routes.delete import delete_routes
from app.auth.signup import auth_routes
from app.page_routes.pages import pages



medsync.register_blueprint(api)
medsync.register_blueprint(post_routes)
medsync.register_blueprint(delete_routes)
medsync.register_blueprint(auth_routes)
medsync.register_blueprint(pages)


