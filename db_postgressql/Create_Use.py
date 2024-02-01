from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date

# Configuration de la connexion à la base de données
engine = create_engine('postgresql+psycopg2://postgres:pass@localhost/test')
metadata = MetaData()

# Définition de la table 'personne'
personne = Table('Use', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('prenom', String(50)),
                 Column('nom', String(50)),
                 Column('date_naissance', Date)
                 )

# Création de la table dans la base de données
metadata.create_all(engine)