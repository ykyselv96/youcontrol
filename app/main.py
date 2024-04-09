from fastapi import FastAPI
from endpoints import companies
from endpoints import users
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from core.config import system_config
from loguru import logger


app = FastAPI()


origins = ["http://localhost",
           "http://localhost:8000",
           ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    # db = get_db()
    # await db.connect()
    logger.info("Connected to DB")



@app.on_event("shutdown")
async def shutdown():

    # db = get_db()
    # await db.disconnect()
    logger.info("Disconnected from DB")


app.include_router(companies.router)
app.include_router(users.router)



if __name__ == "__main__":
    uvicorn.run('main:app', host=system_config.app_host, port=int(system_config.app_port), reload=True)
