from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["hardmux"]
users = db["users"]

def get_user(user_id):
    return users.find_one({"_id": user_id}) or {}

def update_user(user_id, data):
    users.update_one({"_id": user_id}, {"$set": data}, upsert=True)
