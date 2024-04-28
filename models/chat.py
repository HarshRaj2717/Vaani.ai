from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class Address:
    city: str
    country: str


class Chat(BaseModel):
    name: str
    age: int
    address: Address
