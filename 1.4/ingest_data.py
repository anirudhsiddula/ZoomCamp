#!/usr/bin/env python
# coding: utf-8

import os
import argparse

from time import time

import pandas as pd
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    url = params.url


    csv_name = url.split('/')[-1]
    
    print(f"Downloading {url} to {csv_name}")
    
    os.system(f"wget {url}")


    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df = next(df_iter)

    df_findtimestamp = pd.read_csv(csv_name, nrows=10)
    timestamp_columns = []
    for column in df_findtimestamp.columns:
        if df_findtimestamp[column].apply(lambda x: isinstance(x, str) and pd.to_datetime(x, errors='coerce') is not pd.NaT).all():
            df[column] = pd.to_datetime(df[column])
            timestamp_columns.append(column)

    # Replace non-alphanumeric characters with "_"
    #table_name = ''.join(c if c.isalnum() else "_" for c in csv_name)
    table_name = ''.join("" if c.isnumeric() else c for c in csv_name)
    table_name = ''.join(c if c.isalpha() else "_" for c in csv_name)
    table_name = '_'.join(filter(None, table_name.split('_')))
    table_name = table_name.replace("_csv_gz", "")
    table_name = table_name.replace("_csv", "")

    # Print the modified table name
    print(f"Table name: {table_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df.to_sql(name=table_name, con=engine, if_exists='append')


    while True: 

        try:
            t_start = time()
            
            df = next(df_iter)

            for column in timestamp_columns:
                df[column] = pd.to_datetime(df[column])

            df.to_sql(name=table_name, con=engine, if_exists='append')

            t_end = time()

            print('inserted another chunk, took %.3f second' % (t_end - t_start))

        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)
