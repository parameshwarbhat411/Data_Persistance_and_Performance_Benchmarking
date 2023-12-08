import time
import psutil
from sql_loader.query_sql import query_sql
from mongodb_loader.query_mongo import query_mongodb
from neo4j_loader.query_neo4j import query_neo4j
import queries

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().used

def measure_query_time(func, *args):
    start_time = time.time()
    try:
        func(*args)
    except Exception as e:
        print(f"Error during query execution: {str(e)}")
        return None
    end_time = time.time()
    return end_time - start_time

def run_benchmarks():
    times_data = {}
    cpu_usage_data = {}
    memory_usage_data = {}
    error_data = {}

    query_names = queries.sql_queries.keys()

    for query_name in query_names:
        # MongoDB
        print("Running MongoDB query")
        mongo_query = queries.mongodb_queries[query_name]
        mongo_time = measure_query_time(
            query_mongodb,
            mongo_query["query_type"],
            mongo_query["query"],
            mongo_query.get("limit"),
            mongo_query.get("sort")
        )
        mongo_cpu = get_cpu_usage()
        mongo_memory = get_memory_usage()
        print("Finished MongoDB query")

        # SQL
        print("Running SQL query")
        sql_time = measure_query_time(query_sql, queries.sql_queries[query_name])
        sql_cpu = get_cpu_usage()
        sql_memory = get_memory_usage()
        print("Finished SQL query")

        # Neo4j
        print("Running Neo4j query")
        neo4j_time = measure_query_time(query_neo4j, queries.neo4j_queries[query_name])
        neo4j_cpu = get_cpu_usage()
        neo4j_memory = get_memory_usage()
        print("Finished Neo4j query")

        times_data[query_name] = {"SQL": sql_time, "MongoDB": mongo_time, "Neo4j": neo4j_time}
        cpu_usage_data[query_name] = {"SQL": sql_cpu, "MongoDB": mongo_cpu, "Neo4j": neo4j_cpu}
        memory_usage_data[query_name] = {"SQL": sql_memory, "MongoDB": mongo_memory, "Neo4j": neo4j_memory}
        # error_data[query_name] = {
        #     "SQL": sql_time is None,
        #     "MongoDB": mongo_time is None,
        #     "Neo4j": neo4j_time is None
        # }

    return times_data, cpu_usage_data, memory_usage_data, query_names

# if __name__ == "__main__":
#     query_times, cpu_usages, memory_usages, errors, queries = run_benchmarks()
#     # Process or display the results


