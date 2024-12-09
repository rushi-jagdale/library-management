from typing import TypedDict

class Book(TypedDict):
    id: int
    title: str
    author: str
    published_year: int

class Member(TypedDict):
    id: int
    name: str
    email: str
    phone: str
