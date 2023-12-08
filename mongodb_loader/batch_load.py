import pandas as pd
from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Function to load data in batches
def load_data_in_batches_mongo(file_path, batch_size,total_records_limit):
    total_records_processed = 0
    for chunk in pd.read_csv(file_path, chunksize=batch_size):
        collection.insert_many(chunk.to_dict('records'))
        total_records_processed += batch_size
        print(f"Processed {total_records_processed} records...")
        if total_records_processed >= total_records_limit:
            break
# # Set the batch size and file path
# batch_size = 100000  # Adjust the batch size as needed
# file_path = '../data/2020_Yellow_Taxi_Trip_Data_20231129.csv'
#
# # Start the batch loading process
# load_data_in_batches(file_path, batch_size)
