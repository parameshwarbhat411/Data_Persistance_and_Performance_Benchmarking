from neo4j import GraphDatabase

from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

# Connect to Neo4j
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))


def load_batch(tx, file_path, skip, limit):
    query = """     
    LOAD CSV WITH HEADERS FROM 'file:///' + $file_path AS row
    WITH row LIMIT $limit
    WHERE row.VendorID IS NOT NULL AND row.PULocationID IS NOT NULL AND row.DOLocationID IS NOT NULL

    // Create or merge Vendor nodes
    MERGE (v:Vendor { id: row.VendorID })

    // Create or merge Pickup and Dropoff Location nodes
    MERGE (pickup:Location { id: row.PULocationID })
    MERGE (dropoff:Location { id: row.DOLocationID })

    // Create a Trip node for each row
    CREATE (trip:Trip {
        pickup_datetime: row.tpep_pickup_datetime,
        dropoff_datetime: row.tpep_dropoff_datetime,
        passenger_count: toInteger(row.passenger_count),
        trip_distance: toFloat(row.trip_distance),
        rate_code: toInteger(row.RatecodeID),
        store_and_fwd_flag: row.store_and_fwd_flag,
        payment_type: toInteger(row.payment_type),
        fare_amount: toFloat(row.fare_amount),
        extra: toFloat(row.extra),
        mta_tax: toFloat(row.mta_tax),
        tip_amount: toFloat(row.tip_amount),
        tolls_amount: toFloat(row.tolls_amount),
        improvement_surcharge: toFloat(row.improvement_surcharge),
        total_amount: toFloat(row.total_amount),
        congestion_surcharge: toFloat(row.congestion_surcharge)
    })

    // Create relationships
    MERGE (v)-[:OPERATED]->(trip)
    MERGE (trip)-[:STARTED_AT]->(pickup)
    MERGE (trip)-[:ENDED_AT]->(dropoff)
    """
    tx.run(query, file_path=file_path, skip=skip, limit=limit)


def load_data_in_batches_neo4j(file_path, batch_size, total_records_limit):
    total_records_processed = 0
    with driver.session() as session:
        while True:
            session.write_transaction(load_batch, file_path, total_records_processed, batch_size)
            total_records_processed += batch_size
            print(f"Processed {total_records_processed} records...")
            # Check if end of file is reached (e.g., by checking the number of processed rows in the batch)
            # Break the loop if the total records limit is reached
            if total_records_processed >= total_records_limit:
                break


# Define the batch size and file path
# batch_size = 50000  # Adjust the batch size as needed
# file_path = '../data/2020_Yellow_Taxi_Trip_Data_20231129.csv'
#
# # Start the batch loading process
# load_data_in_batches(file_path, batch_size)

driver.close()
