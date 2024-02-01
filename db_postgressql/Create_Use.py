from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
import pandas as pd

engine = create_engine('postgresql+psycopg2://postgres:pass@localhost/test')
 


def storge_table():
     
    Data = pd.read_csv('../src/datasets/UpdatedResumeDataSet.csv' ,encoding='utf-8')
    Data.to_sql('CV', engine, index=False, if_exists='replace')  
    engine.dispose()
