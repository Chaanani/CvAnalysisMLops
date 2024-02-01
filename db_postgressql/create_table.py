from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import psycopg2
"""

user = 'postgres' 
password = 'sma3@MOU'
host = 'localhost'  
port = '5433'
dbname = 'Test'

url_connexion = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
engine = create_engine(url_connexion)





try:
    with engine.connect() as conn:
        print("Connexion à la base de données réussie!")
except Exception as e:
    print("Impossible de se connecter à la base de données.")
    print("Détails de l'erreur :")
    print(e)
"""

conn = psycopg2.connect(
        user = 'postgres', 
        password = 'pass',
        host = 'localhost',  
        dbname = 'test')

cur =conn.cursor()

cur.execute(""" CREATE TABLE personne(
            id int,
            prenom VARCHAR(50),
            nom VARCHAR(50),
            data_naissance DATE) """)


cur.close()
conn.commit()
conn.close()