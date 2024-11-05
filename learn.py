# https://fastapi.tiangolo.com/python-types/#dict

#Declaring types
# Simple Types: int, float, bool, bytes, str
def get_name_with_age(name: str, age: int): # Declare the type of the variable that is required for the function.

    name_with_age = name + " is this old: " + str(age)
    return name_with_age

# Generic types: dict, list, set, tuple
# Internal values can have their own types: list[str] Internal types are called 'type parameters'
# Depending on version, you may or may not need to import typing

def process_items(items: list[str]):
    for item in items:
        print(item)

def process_itemz(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

# To define a dict, you pass 2 type parameters, separated by commas.

def process_items_(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

# In 3.10 you can declare multiple typings

def process_item(item: int | str):
    print(item)

# With typing you can declare an Optional = None. An input is still required but the value can be None without throwing an error

from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

# In 3.10 you can just do a union like so str | None

def say_hi(name: str | None):
    print(f"Hey {name}!")



# Pydantic

from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123

# You can alos add annotations as metadata that are used by other programs

from typing import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"