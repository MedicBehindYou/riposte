from sqlalchemy.exc import SQLAlchemyError
from .misc import send_email
from fastapi import HTTPException

recipients = ['esmith@impactnetworking.com', 'sredman@impactnetworking.com']

def execute(token, riposteSubmit, db):
    if token == "H7945TORTX2MGBWP1SYN0W1WL27IAG4G":
        if 'Running' in riposteSubmit.output:
            Subject = "ATP detected on Device" + riposteSubmit.hostname
            Body = riposteSubmit.token + "\n" + riposteSubmit.hostname + "\n" + riposteSubmit.ip + "\n" + riposteSubmit.output
            send_email(Subject, Body, recipients)
        try:
            db.add(riposteSubmit)
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            print(f"An error occurred: {e}")
            raise HTTPException(status_code=500, detail="Database error")
    elif token == "82D7GOY6LEAT6WFZTDVLX7Z2J71C5NSJ":
        if 'SCCM Found: ccmsetup.exe' in riposteSubmit.output:
            Subject = "SCCM detected on Device" + riposteSubmit.hostname
            Body = riposteSubmit.token + "\n" + riposteSubmit.hostname + "\n" + riposteSubmit.ip + "\n" + riposteSubmit.output
            send_email(Subject, Body, recipients)
        try:
            db.add(riposteSubmit)
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            print(f"An error occurred: {e}")
            raise HTTPException(status_code=500, detail="Database error")