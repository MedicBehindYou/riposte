#run.py
from app.models import Base, engine
import uvicorn

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=1984, reload=True)