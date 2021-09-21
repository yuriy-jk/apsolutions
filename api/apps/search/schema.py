from datetime import datetime

from web.schema import BaseSchema
from marshmallow_dataclass import dataclass


@dataclass
class Search(BaseSchema):
    text: str


@dataclass
class Post(BaseSchema):
    id: int
    rubrics: str
    text: str
    created_date: datetime


@dataclass
class Delete(BaseSchema):
    id: int
