from pymongo import MongoClient


class ConectionMongo:

    client = MongoClient()
    db = client["tennisDb"]
    collection = db["tournaments"]