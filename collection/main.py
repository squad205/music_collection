# import os
from fastapi import FastAPI
from routers import inventory
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(inventory.router)

# os.environ.get("CORS_HOST", None),
origins = [
    "http://localhost:3000",
    "CORS_HOST",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
