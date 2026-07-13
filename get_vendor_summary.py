from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import logging
import time
from ingestion_db import ingest_db
import os
from dotenv import load_dotenv


logging.basicConfig(
    filename = "logs/get_vendor_summary.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s -%(message)s",
    filemode = "a",
    force=True
)


load_dotenv()

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT"))
database = os.getenv("DB_NAME")

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)


# firstly creating vendor summary and then cleaning it.

def create_vendor_summary(engine):
    '''this func will merge the different tables to get the overall vendor summary and adding new columns in the resultant data'''
    df = pd.read_sql_query("""
        WITH FreightSummary as (
            SELECT
                VendorNumber,
                SUM(Freight) as FreightCost
            FROM vendor_invoice
            GROUP BY VendorNumber
        ),
        
        PurchaseSummary as (
            SELECT 
                p.VendorNumber,
                p.VendorName,
                p.Brand,
                p.Description,
                p.PurchasePrice,
                pp.Price as ActualPrice,
                pp.Volume,
                Sum(p.Quantity) as TotalPurchaseQuantity, 
                SUM(p.Dollars) as TotalPurchaseDollars
            FROM purchases p
            JOIN purchase_prices pp
                ON p.Brand = pp.Brand
            WHERE p.PurchasePrice > 0
            GROUP BY p.VendorNumber,p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume
        ),
        
        SalesSummary as (
            SELECT
                VendorNo,
                Brand,
                SUM(SalesPrice) as TotalSalesPrice,
                SUM(SalesDollars) as TotalSalesDollars,
                SUM(SalesQuantity) as TotalSalesQuantity,
                SUM(ExciseTax) as TotalExciseTax
            FROM sales
            GROUP BY VendorNo, Brand
        )
        
        SELECT
            ps.VendorNumber,
            ps.VendorName,
            ps.Brand,
            ps.Description,
            ps.PurchasePrice,
            ps.ActualPrice,
            ps.Volume,
            ps.TotalPurchaseQuantity, 
            ps.TotalPurchaseDollars,
            ss.TotalSalesPrice,
            ss.TotalSalesDollars,
            ss.TotalSalesQuantity,
            ss.TotalExciseTax,
            fs.FreightCost
        FROM PurchaseSummary ps
        LEFT JOIN SalesSummary ss
            ON ps.VendorNumber = ss.VendorNo
            AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummary fs
            ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseDollars DESC
        """, engine)

    return df


def clean_data(df):
    '''this func will clean the data'''

    # changing dtype
    df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')

    # removing extra spaces from categorical columns
    df["VendorName"] = df["VendorName"].fillna("").str.strip()
    df["Description"] = df["Description"].fillna("").str.strip()

    # creating new columns/features for better analysis
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars']) * 100
    df['StockTurnover'] =  df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalesToPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']

    # Replacing inf/-inf with 0
    df = df.replace([np.inf, -np.inf], np.nan).fillna(0)

    return df

if __name__ == '__main__':
    
    try:
        start = time.time()
        logging.info(f"Start time : {start}")
        logging.info('Creating Vendor Summary Table...')
        summary_df = create_vendor_summary(engine)
    
        logging.info('Cleaning Data...')
        clean_df = clean_data(summary_df)
    
        logging.info('Ingesting data...')
        ingest_db(clean_df, 'vendor_sales_summary', engine)
        logging.info("Vendor summary uploaded successfully. Total rows: %d",len(clean_df))

        end = time.time()
        logging.info(f"End time : {end}")
        total_time = (end-start) / 60
        logging.info(f"Total time taken : {total_time:.2f} minutes")
        
    except Exception as e:
        logging.exception("Vendor summary generation failed: %s", e)

    finally:
        engine.dispose()
        logging.info("Database connection closed.")