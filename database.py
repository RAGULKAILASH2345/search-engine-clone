from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def get_db_connection():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        client.admin.command("ismaster")
        print("Connected to DB!!!")
        return client.search_engine
    except ConnectionFailure:
        print("Failed to connect!!!")
        return None
    
if __name__ == "__main__":
    resp = get_db_connection()
    print(resp)