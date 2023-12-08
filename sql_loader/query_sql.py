import pymysql
import sql_loader.sql_config as config

def query_sql(query):
    connection = pymysql.connect(
        host=config.SQL_LH,
        port=config.SQL_PORT,
        user=config.SQL_USER,
        password=config.SQL_PASSWORD,
        db=config.SQL_DB,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)

            # Identifying the type of query
            if query.strip().lower().startswith("select"):
                # Fetch and return data for SELECT queries
                result = cursor.fetchall()
            else:
                # For non-select queries, commit changes and return nothing or the number of affected rows
                connection.commit()
                result = cursor.rowcount

            return result
    except pymysql.MySQLError as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        connection.close()