import pandas as pd
from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Load CSV data
df = pd.read_csv('../data/2020_Yellow_Taxi_Trip_Data_20231129.csv')

# Load data into MongoDB
collection.insert_many(df.to_dict('records'))
