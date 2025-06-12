#app/routes.py
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from app.models import Riposte, engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Token
from .action import execute
import datetime


router = APIRouter()
sessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

class riposteClass(BaseModel):
    ticket: str
    hostname: str
    ip: str
    mac: str
    pubip: str
    output: str

@router.post("/riposte/{token}")
async def riposteRoute(token, riposteSubmission: riposteClass, db: Session = Depends(get_db)):
    riposteSubmit = Riposte(
        token=token,
        ticket=riposteSubmission.ticket, 
        hostname=riposteSubmission.hostname, 
        ip=riposteSubmission.ip, 
        mac=riposteSubmission.mac,
        pubip=riposteSubmission.pubip,
        output=riposteSubmission.output,
        time=datetime.datetime.now(),
        result='0'
    )

    tokenCheck = db.query(Token).filter(Token.token == token).first() is not None

    if tokenCheck:
        expiryDate = db.query(Token.expiry).filter(Token.token == riposteSubmit.token)
        result = expiryDate.first()[0]
        expiryCheck = db.query(Token).filter(Token.token == riposteSubmit.token, datetime.date.today() < datetime.datetime.strptime(result, "%d/%m/%Y").date()).first() is not None
        
        if expiryCheck:
            response = execute(token, riposteSubmit, db)
        else:
            raise HTTPException(status_code=404, detail="Token not found")
    else:
        raise HTTPException(status_code=404, detail="Token not found")

    return response