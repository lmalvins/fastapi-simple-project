from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class Book(BaseModel):
    id: str
    title: str
    author: str
    category: str
