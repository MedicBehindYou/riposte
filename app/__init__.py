#app/__init__.py
from fastapi import FastAPI
from .routes import router
from .misc import load_config

app = FastAPI()
app.include_router(router)
config = load_config()

if config:
    SQL_STRING = (config['General']['sql_string'])
    SMTP_USER = (config['General']['smtp_user'])
    SMTP_PASS = (config['General']['smtp_pass'])

__all__ = ['app']