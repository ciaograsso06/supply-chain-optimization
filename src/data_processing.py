import pandas as pd
import os
from dotenv import load_dotenv

def load_data():
    load_dotenv()
    dataset_path = os.getenv("DATASET_PATH")
    df_sales = pd.read_csv(f'{dataset_path}/train.csv')
    df_features = pd.read_csv(f'{dataset_path}/features.csv')
    df_stores = pd.read_csv(f'{dataset_path}/stores.csv')
    return df_sales, df_features, df_stores

def preprocess_data(df_sales, df_features, df_stores):
    df = df_sales.merge(df_stores, on='Store').merge(df_features, on=['Store', 'Date'])
    df['Date'] = pd.to_datetime(df['Date'])
    return df.sort_values(by=['Store', 'Date'])