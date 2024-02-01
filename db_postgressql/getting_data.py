from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
import pandas as pd

engine = create_engine('postgresql+psycopg2://postgres:pass@localhost/test')
 
def extract_table():
     
    query = "SELECT * FROM CV"
    df = pd.read_sql_query(query, engine)
    df.to_csv('../src/datasets/UpdatedResumeDataSet.csv', index=False)
    engine.dispose()