import pandas as pd
import sqlalchemy
from config import SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DB

# Create SQL engine
engine = sqlalchemy.create_engine(f'mysql+://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}/{SQL_DB}')

# Load CSV data
df = pd.read_csv('../data/2020_Yellow_Taxi_Trip_Data_20231129.csv')

# Load data into SQL
df.to_sql('yellow_taxi_data', con=engine, if_exists='replace', index=False)
