import sqlite3
import sqlalchemy
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = sqlalchemy.create_engine("sqlite:///clients.db")
base = declarative_base()
session = sessionmaker(bind=engine)()

class Client(base):
    __tablename__ = "client"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    lastname = Column(String)

def create_schema():
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)

def search_client(id, name , lastname):
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(Client).filter(Client.id == id).first()

    if (query is None):
        query = session.query(Client).filter(Client.name == name).first()

        if(query is None):
            query = session.query(Client).filter(Client.lastname == lastname).first()
            if (query is None):
                query = ('No existe el usuario')
    
    return query
    print(query)


    session.commit()




if __name__ == "__main__":
  # Crear DB
  create_schema()

  search_client(1)

