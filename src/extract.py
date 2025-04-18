import pandas as pd
import os

# Phase 1: Extracting the data
# importing packages, pandas to read file, and os to check whether the file exists

#create function extract_fxn
def extract_fxn(filepath):
    """
    Extracting the NYC Taxi data, from the month of January to a dataframe.
    Args: 
        filepath(str) : specifies the path through which the parquet file is accessed, pyarrow and pandas can read its binary contents
    Returns: 
        a pandas dataframe
    """

    #os checks if file is found and if not
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found at {filepath}, which is the specified location")
    
    #the else block checks only when os finds a file
    df = pd.read_parquet(filepath)
    print(f"Data loaded onto dataframe successfully with shape {df.shape}")
    return df

"""
    every py script has a default variable 'name', if we run this section we run the test code
    we extract data and load to df but if we run the function as imported to other 
    files we just use the function and manipulate the data therein
"""

if __name__ ==  "__main__":
    #specified entire path bc of relative path resolution issues
    data_loaded = "E:/dev/DE/Final Project/codebase/nyc-taxi-etl-pipeline/data/yellow_tripdata_2023-01.parquet"
    df = extract_fxn(data_loaded)

    #peek at the shape of the dataset, unpack the tuple
    rows, columns = df.shape
    print(f"The shape of the raw data is {rows} rows and {columns} columns")

    print("\n Columns present in the dataset are as listed:")
    print(df.columns.to_list())

    print("\n\n The first 5 rows of the raw data are as follows:")
    print(df.head())



