from pymongo import MongoClient


# MongoDB hierarchy:
# - cluster/instance --> db --> collection --> document/post(dictionary) --> key --> value

cluster = MongoClient('mongodb://127.0.0.1:27017/?appname=PyMongo%20Client') # Here appname=PyMongo%20Client --> the name of the application/client connecting to MongoDB server.
db = cluster["company"]
collection = db["users"]

# _id:
# - Each document/post is uniquely identified by _id.
# - If you don't specify _id, MongoDB will generate a unique random value for _id.
# - Ex: _id: ObjectId("60f158b76e5d66174224b9aa")

# - Without _id
post = {"name": "tim", "age": 27, "email": "tim@gmail.com"}
# - With _id
post0 = {"_id": 0, "name": "cook", "age": 35, "email": "cook@gmail.com"}
post1 = {"_id": 1, "name": "ram", "age": 35, "email": "ram@yahoo.com"}
post2 = {"_id": 2, "name": "sham", "age": 46, "email": "sham@gmail.com"}
post3 = {"_id": 3, "name": "bob", "age": 46, "email": "bob@yahoo.com"}

