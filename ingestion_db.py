print("Program Started")


import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time
from dotenv import load_dotenv

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)


# logging
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)


load_dotenv()

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT"))
database = os.getenv("DB_NAME")

# MYSQL connection
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)



def ingest_db(df, table_name, engine):
    """This function ingests the dataframe into the database table."""
    df.to_sql(table_name, con=engine, if_exists='replace', index=False, chunksize=5000,
        method="multi")



def load_raw_data():
    print("Inside load_raw_data()")

    """This function loads CSV files as DataFrames and ingests them into MySQL."""
    start = time.time()

    print("Checking data folder...")

    for file in os.listdir("data"):
        print(f"Found file: {file}")

        if file.endswith(".csv"):

            print(f"Reading {file}")
            df = pd.read_csv(os.path.join("data", file))

            print(f"Uploading {file} to MySQL...")

            logging.info(f"Ingesting {file} in MySQL db")
            ingest_db(df, file[:-4], engine)

            print(f"{file} uploaded successfully!")

    end = time.time()
    total_time = (end - start) / 60


    print("Finished!")

    logging.info("-------------------Ingestion Complete-------------------")
    logging.info(f"Total time taken: {total_time:.2f} minutes")

if __name__ == "__main__":
    try:
        load_raw_data()
        
    except Exception as e:
        logging.exception("Vendor summary generation failed: %s", e)

    finally:
        engine.dispose()
        logging.info("Database Connection Closed")