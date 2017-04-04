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

print('Insertion:')
print("-------------------------------------------------")

print('- Inserting one document/post at a time: ')
insert_one_result = collection.insert_one(post)
print('inserted_id: {}'.format(insert_one_result.inserted_id))
insert_one_result = collection.insert_one(post0)
print('inserted_id: {}'.format(insert_one_result.inserted_id))
print("-------------------------------------------------")

print('- Inserting multiple documents/posts at a time: ')
insert_many_result = collection.insert_many([post1, post2, post3])
print('inserted_ids: {}'.format(insert_many_result.inserted_ids))
print("-------------------------------------------------")

