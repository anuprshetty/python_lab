from pymongo import MongoClient


# MongoDB hierarchy:
# - cluster/instance --> db --> collection --> document/post(dictionary) --> key --> value

cluster = MongoClient('mongodb://127.0.0.1:27017/?appname=PyMongo%20Client') # Here appname=PyMongo%20Client --> the name of the application/client connecting to MongoDB server.
db = cluster["company"]
collection = db["users"]

