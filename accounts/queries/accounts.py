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

class AccountOutWithPassword(AccountOut):
    hashed_password: str

class DuplicateAccountError(ValueError):
    pass




#get all is for administrator side only at this time
class AccountRepo:
    def get_all(self) -> List[AccountOutWithPassword]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                        , first_name
                        , last_name
                        , email
                        , hashed_password
                        FROM accounts
                        ORDER BY id;
                        """
                    )
                    return [
                        self.record_to_account_out(record) for record in result
                    ]
        except Exception as e:
            print(e)
            return {
                "message": "Could not retrieve all accounts. Please try again."
            }


        

def account_in_to_out(self, id: int, account: AccountIn):
    old_data = account.dict()
    return AccountOut(id=id, **old_data)

def record_to_account_out(self, record):
    return AccountOutWithPassword(
        id=record[0],
        first_name=record[1],
        last_name=record[2],
        email=record[3],
        hashed_password=record[4],
    )
