from sqlalchemy.exc import SQLAlchemyError
from .misc import send_email
from fastapi import HTTPException
import os

recipients = ['esmith@impactnetworking.com', 'sredman@impactnetworking.com']

def execute(token, riposteSubmit, db):
    path = os.path.join(os.path.dirname(__file__), 'config', 'scripts', token)
    with open(path) as f:
        s = f.read()
    exec(s)