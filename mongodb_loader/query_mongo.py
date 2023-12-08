from pymongo import MongoClient
import config

def query_mongodb(query_type, query, limit=None, sort=None):
    client = MongoClient(config.MONGO_URI)
    db = client[config.MONGO_DB]
    collection = db[config.MONGO_COLLECTION]

    try:
        if query_type == 'aggregate':
            result = list(collection.aggregate(query))
        elif query_type == 'find':
            result_query = collection.find(query)
            if sort:
                result_query = result_query.sort(sort)
            if limit is not None:
                result_query = result_query.limit(limit)
            result = list(result_query)
        elif query_type == 'update':
            result = collection.update_many(query[0], query[1])  # Expecting query to be a tuple of (filter, update)
        elif query_type == 'delete':
            result = collection.delete_many(query)  # Expecting query to be a deletion filter
        elif query_type == 'count':
            result = collection.count_documents(query)
        else:
            raise ValueError("Invalid query type specified")
    except Exception as e:
        print(f"An error occurred: {e}")
        result = []
    finally:
        client.close()

    return result

if __name__ == "__main__":
    # Example query
    query = [
            {"$group": {"_id": "$DOLocationID", "total_revenue": {"$sum": "$total_amount"}}}
        ]
    result = query_mongodb("aggregate", query, limit=10)
    print(result)