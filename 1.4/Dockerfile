FROM python:3.9

WORKDIR /app
RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

COPY ingest_data.py /app/ingest_data.py
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]