from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
import pandas as pd

engine = create_engine('postgresql+psycopg2://postgres:pass@localhost/test')
 



def récupere_table():
     
    query = "SELECT * FROM CV"
    df = pd.read_sql_query(query, engine)
    engine.dispose()

    return df


df = récupere_table()

df.to_csv('../src/datasets/UpdatedResumeDataSet.csv', index=False)
