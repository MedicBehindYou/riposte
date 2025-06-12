from sqlalchemy.exc import SQLAlchemyError  # noqa: F401
from .misc import send_email  # noqa: F401
from fastapi import HTTPException  # noqa: F401
import os
import datetime # noqa: F401

response = {"message": "Script Returned No Response"}

def execute(token, riposteSubmit, db):
    path = os.path.join(os.path.dirname(__file__), 'config', 'scripts', token)
    with open(path) as f:
        s = f.read()

    local_vars = {
        "riposteSubmit": riposteSubmit,
        "db": db,
        "response": {"message": "Script Returned No Response"}
    }
    
    exec(s, {}, local_vars)
    return local_vars["response"]