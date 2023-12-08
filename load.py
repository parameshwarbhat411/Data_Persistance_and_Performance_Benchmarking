from config import TOTAL_RECORDS_LIMIT, BATCH_SIZE, BATCH_SIZE_NEO
from mongodb_loader.batch_load import load_data_in_batches_mongo
from neo4j_loader.batch_load import load_data_in_batches_neo4j
from sql_loader.batch_load import load_data_in_batches_sql


def load():
    # Set the batch size, file path, and total records limit
    batch_size = BATCH_SIZE  # Adjust the batch size as needed
    batch_size_neo4j = BATCH_SIZE_NEO
    file_path = 'data/2020_Yellow_Taxi_Trip_Data_20231129.csv'
    total_records_limit = TOTAL_RECORDS_LIMIT  # Limit to 5 million records

    # Start the batch loading process
    print("Loading Neo4j data...")
    load_data_in_batches_neo4j(file_path, batch_size_neo4j, total_records_limit)
    print("Neo4j data loaded")
    print("Loading SQL data...")
    load_data_in_batches_sql(file_path, batch_size, total_records_limit)
    print("SQL data loaded")
    print("Loading MongoDB data...")
    load_data_in_batches_mongo(file_path, batch_size, total_records_limit)
    print("MongoDB data loaded")


# if __name__ == "__main__":
#     main()
