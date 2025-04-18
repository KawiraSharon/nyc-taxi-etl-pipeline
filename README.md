# nyc-taxi-etl-pipeline
An ETL pipeline for the NYC Taxi Data that leverages Python, PostgreSQL, Docker and Kestra for the Final Project for CIS 660 - Data Engineering.

The essence of this project is to enrich knowledge in;
The ETL Process which is meant to:
Extract - load the data to a dataframe, real life case scenario, move from an overall cloth container to a closet for ease of use and manipulation. (Reads parquet to RETURN DF)
Transform - manipulate the data by cleaning, organizing and enriching it so it is usable. (Cleans and filters df to RETURN clean DF)
Load - save to database so that applications, systems can use it. ( PUSHES new_df to PostgreSQL and RETURNS nothing)

