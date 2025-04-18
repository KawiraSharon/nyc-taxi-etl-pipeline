import pandas as pd
import psycopg2 # connects to postgres using sqlalchemy
from sqlalchemy import create_engine # connects pd to postgres
from transform import transform_data
from extract import extract_fxn

def load_df(new_df, db, user, password, host, port, table):
    """
    Uses SQLAlchemy to load the enriched df, new_df to the postgres table
    Args:
        new_df(Dataframe): the transformed dataframe
        db(str): name assigned to postgresql db in yaml file for db authentication
        user(str): username assigned in yaml for db authentication
        password(str): pass in yaml for db authentication
        host(str): localhost 127.0.0.1
        port(str): default port postgres is listening at
        table(str): table to be created for postgres
    Return:
        nothing because the function just loads data to postgresql and is not aimed at returning anything
    """

    try: 
        connection_str = f"postgresql://{user}:{password}@{host}:{port}/{db}"
        # connection_str = "postgresql://postgres:postgres@host.docker.internal:5432/nyc_taxi_db"
        engine = create_engine(connection_str)
        print(f"Connection to database found at {port} on {host}")
        new_df.to_sql(table, engine, if_exists='replace', index=False)
        print(f"Successfully loaded onto database and table {table} with {len(new_df)} rows.")

    except Exception as e:
        print(f"Dataframe not loaded successfully: {e}")

if __name__ == "__main__":
    data_path = "E:/dev/DE/Final Project/codebase/nyc-taxi-etl-pipeline/data/yellow_tripdata_2023-01.parquet"
    raw_df = extract_fxn(data_path)
    new_df = transform_data(raw_df)

    db = "nyc_taxi_db"
    user = "postgres"
    password = "postgres"
    host = "host.docker.internal" #"localhost"
    port = "5432"
    table = "nyc_january_taxi_data"

    print("Connecting to host:", host)


    load_df(new_df, db, user, password, host, port, table)
