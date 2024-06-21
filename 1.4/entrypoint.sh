#!/bin/zsh

#First table load
python /app/ingest_data.py --host=pgdatabase_1 --port=5432 --db=ny_taxi --user=root --password=root --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"

#Second table load
python ingest_data.py --host=pgdatabase_1 --port=5432 --db=ny_taxi --user=root --password=root --url="https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"