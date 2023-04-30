from typing import List, Optional
from pydantic import BaseModel


class BuchiBase(BaseModel):
    name: str
    description: Optional[str] = None


class BuchiCreate(BuchiBase):
    pass


class Buchi(BuchiBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
