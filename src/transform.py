import pandas as pd
from extract import extract_fxn

def transform_data(df):
    """
    This function transforms the NYC Taxi Data data by:
        dropping null values, that is ghost trips
        normalizing datetime columns
        creating new column, trip_duration
        dropping any trips longer than 3 hrs
    Args:
        (df), returned from the extract file which extracted data from the parquet file
    Return:
        (new_df), cleaned and meaningful dataframe
    """

    # removing ghost trips and trips without passengers
    new_df = df[(df['passenger_count'] > 0) & (df['trip_distance'] > 0)].copy()

    # normalize datetime columns
    new_df['tpep_pickup_datetime'] = pd.to_datetime(new_df['tpep_pickup_datetime'])
    new_df['tpep_dropoff_datetime'] = pd.to_datetime(new_df['tpep_dropoff_datetime'])

    # creating column trip_duration for visualization
    new_df['trip_duration'] = (new_df['tpep_dropoff_datetime'] - new_df['tpep_pickup_datetime']).dt.total_seconds()/60

    # removing trips longer than 180 mins/3hrs
    new_df = new_df[new_df['trip_duration'] <= 180]

    return new_df


# test section
if __name__ == "__main__":
    data_path = "E:/dev/DE/Final Project/codebase/nyc-taxi-etl-pipeline/data/yellow_tripdata_2023-01.parquet"

    raw_df = extract_fxn(data_path)

    new_df = transform_data(raw_df)

    print(f"\n The transformed dataset is of shape {new_df.shape}")
    print("\n The first 5 rows of the transformed dataset are: ")
    print(new_df.head())