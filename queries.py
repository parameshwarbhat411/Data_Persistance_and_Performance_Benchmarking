sql_queries = {
    "select_basic": "SELECT * FROM yellow_taxi_data",
    "total_fare_over_2_miles": "SELECT SUM(fare_amount) FROM yellow_taxi_data WHERE trip_distance > 2",
    "same_pickup_dropOff": "SELECT a.PULocationID,a.DOLocationID FROM yellow_taxi_data a JOIN yellow_taxi_data b ON a.PULocationID = b.DOLocationID WHERE a.trip_distance < 1.0",
    "update_fare":"SELECT *, CASE WHEN passenger_count > 2 THEN fare_amount * 1.1 ELSE fare_amount END AS fare_amount FROM yellow_taxi_data"
    #TODO: Add more SQL queries as needed

}
# Options for MongoDB queries:
# query_type: find, aggregate, count, distinct, update, delete
mongodb_queries = {
    "select_basic": {
        "query_type": "find",  # Specifying the type of query
        "query": {},  # Fetch all documents from a collection
        "limit": None,
        "sort": None
    },
    "total_fare_over_2_miles": {
        "query_type": "aggregate",
        "query": [
            {"$match": {"trip_distance": {"$gt": 2}}},
            {"$group": {"_id": None, "totalFare": {"$sum": "$fare_amount"}}}
        ],
        "limit": None,
        "sort": None
    },

    "same_pickup_dropOff":{
        "query_type": "aggregate",
        "query": [
            {"$match": {"trip_distance": {"$gt": 2}}},
            {"$group": {"_id": None, "totalFare": {"$sum": "$fare_amount"}}}
        ],
        "limit": None,
        "sort": None
    },

    "update_fare": {
        "query_type": "aggregate",
        "query": [
            {
                "$addFields": {
                    "fare_amount": {
                        "$cond": {
                            "if": { "$gt": ["$passenger_count", 2] },
                            "then": { "$multiply": ["$fare_amount", 1.1] },
                            "else": "$fare_amount"
                        }
                    }
                }
            }
        ],
        "limit": None,
        "sort": None
    }
    #TODO: Add more MongoDB queries as needed
}
neo4j_queries = {
    "select_basic": "MATCH (n:Trip) RETURN n ",
    "total_fare_over_2_miles": "MATCH (n:Trip) WHERE n.trip_distance > 2 RETURN SUM(n.fare_amount)",
    "same_pickup_dropOff": "MATCH (t:Trip) WHERE t.trip_distance > 2 RETURN sum(t.fare_amount) AS totalFare",
    "update_fare": "MATCH (t:Trip) SET t.fare_amount = CASE WHEN t.passenger_count > 2 THEN t.fare_amount * 1.1 ELSE t.fare_amount END RETURN t"
    #TODO: Add more Neo4j queries as needed
}

