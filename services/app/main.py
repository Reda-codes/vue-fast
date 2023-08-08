from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.localDbEngine import localStorage

app = FastAPI()
db = localStorage()
elements = ["costumers", "products"]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """ root route to get the whole db object """
    return db.all()

@app.get("/data/{element}")
async def getElement(element):
    """ route to get a element from the local database """
    if element not in elements:
        raise HTTPException(status_code=400, detail={"message": "The data you are looking for doesn't exist", "dataAllowed": elements})
    return db.get(element)

@app.get("/status")
async def getServerStatus():
    """ route to get the server status """
    return {"status": "ALIVE"}