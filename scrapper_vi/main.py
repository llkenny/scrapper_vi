import os
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pandas as pd


def run():
    """Fetch data and plot"""
    fetch()
    plot()


def fetch():
    os.system("cd scrapper_vi")
    os.system("scrapy crawl vi")


def read_db():
    """Read data from db"""
    db_path = 'scrapy_items.db'
    sqlEngine = create_engine('sqlite:///scrapy_items.db', pool_recycle=3600)
    dbConnection = sqlEngine.connect()
    items = pd.read_sql("select * from item", dbConnection)
    dbConnection.close()
    return items


def plot():
    """Plot data"""
    df = read_db()
    df['created_at'] = pd.to_datetime(df["created_at"])
    unique_titles = df['title'].unique()
    dfs = [df[df['title'] == x].reset_index() for x in unique_titles]
    for df in dfs:
        plt.plot(df['created_at'], df['price'], label=df['title'][0])
    
    plt.legend()
    plt.show()
