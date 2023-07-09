from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


def connect_to_database():

    username = os.environ.get("mongo_username")
    password = os.environ.get("mongo_password")

    # connection url
    CONNECTION_URL = "mongodb+srv://{}:{}@cluster0.nr1dxef.mongodb.net/?retryWrites=true&w=majority".format(
        username, password)

    # connect using MongoClient
    client = MongoClient(CONNECTION_URL)

    # return database name
    return client['ecommerce']
