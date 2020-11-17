from pymongo import MongoClient
from faker import Faker
from time import sleep


db = MongoClient("mongodb://localhost:27017")

db_val = db.MyDB1

print(db.list_database_names())

print(db_val.list_collection_names())

fake_obj = Faker()

#print(fake_obj.name())

while True:
    db_val.DataToStore.insert_one({"name":fake_obj.name(),"address":fake_obj.address()})
    sleep(2)


    
