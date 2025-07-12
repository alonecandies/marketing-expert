from pymongo import MongoClient
import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/marketing")
client = MongoClient(MONGODB_URI)
db = client.get_database()

sessions_collection = db["sessions"]
conversations_collection = db["conversations"]
generated_content_collection = db["generated_content"]
