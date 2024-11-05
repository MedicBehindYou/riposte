#app/routes.py
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from app.models import Riposte, engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from .misc import send_email


router = APIRouter()
sessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

class riposteClass(BaseModel):
    hostname: str
    ip: str
    mac: str
    output: str

@router.post("/riposte/{token}")
async def riposteRoute(token, riposteSubmission: riposteClass, db: Session = Depends(get_db)):
    riposteSubmit = Riposte(
        token=token, 
        hostname=riposteSubmission.hostname, 
        ip=riposteSubmission.ip, 
        mac=riposteSubmission.mac, 
        output=riposteSubmission.output
    )

    return riposteSubmit