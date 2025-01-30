#app/models.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from .misc import load_config

config = load_config()

if config:
    SQL_STRING = (config['General']['sql_string'])

engine = create_engine(SQL_STRING)
Base = declarative_base()

class Riposte(Base):
    __tablename__ = 'riposte'
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(32), index=True)
    hostname = Column(String(256), index=True)
    ip = Column(String(256), index=True)
    mac = Column(String(256), index=True)
    pubip = Column(String(256), index=True)
    output = Column(Text, index=True)
    time = Column(Text, index=True)

class Token(Base):
    __tablename__ = 'token'
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(32), index=True)
    expiry = Column(String(32), index=True)
    description = Column(Text, index=True)