from pymongo import MongoClient
from faker import Faker
from time import sleep


db = MongoClient("mongodb://localhost:27017")

db_val = db.MyDB1

a = db_val.DataToStore.find()

print(a)




    
