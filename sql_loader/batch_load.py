import pandas as pd
from sqlalchemy import create_engine

from config import SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DB

# SQL connection
engine = create_engine(f'mysql+pymysql://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}/{SQL_DB}')

# Function to load data in batches
def load_data_in_batches_sql(file_path, batch_size, total_records_limit):
    total_records_processed = 0
    for chunk in pd.read_csv(file_path, chunksize=batch_size):
        chunk.to_sql('yellow_taxi_data', con=engine, if_exists='append', index=False)
        total_records_processed += len(chunk)
        print(f"Processed {total_records_processed} records...")

        # Break the loop if the total records limit is reached
        if total_records_processed >= total_records_limit:
            break

# Set the batch size, file path, and total records limit
# batch_size = 1000000  # Adjust the batch size as needed
# file_path = '../data/2020_Yellow_Taxi_Trip_Data_20231129.csv'
# total_records_limit = 5000000  # Limit to 5 million records
#
# # Start the batch loading process
# load_data_in_batches_sql(file_path, batch_size, total_records_limit)
