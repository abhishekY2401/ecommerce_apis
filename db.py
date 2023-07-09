from pymongo import MongoClient


def connect_to_database():
    # connection url
    CONNECTION_URL = "mongodb+srv://yadavabhishek6064:Abhiraj123@cluster0.nr1dxef.mongodb.net/?retryWrites=true&w=majority"

    # connect using MongoClient
    client = MongoClient(CONNECTION_URL)

    # return database name
    return client['ecommerce']
