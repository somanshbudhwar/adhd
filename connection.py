
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

access = json.load(open("private_key.json"))

uri = f"mongodb+srv://{access['user_id']}:{access['password']}@cluster-llm.wyaaoj6.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)