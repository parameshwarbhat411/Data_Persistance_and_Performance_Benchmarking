from neo4j import GraphDatabase
import config

class Neo4jQuery:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query):
        with self.driver.session() as session:
            try:
                result = session.run(query)
                return [record for record in result]
            except Exception as e:
                print(f"An error occurred: {e}")
                return []

def query_neo4j(query):
    neo4j_query = Neo4jQuery(config.NEO4J_URI, config.NEO4J_USER, config.NEO4J_PASSWORD)
    try:
        return neo4j_query.run_query(query)
    finally:
        neo4j_query.close()
