from pydantic import BaseModel
from queries.pool import pool
from typing import List

class AccountIn(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    #look into adding optional fields eg: profile pic, fave genre for expansion

class AccountOut(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
