from django.contrib.auth.models import User
from ninja import Schema

from typing import List
from datetime import datetime

class UserSchema(Schema):
    id: int
    email: str
    username: str

class PostSchema(Schema):
    '''Схема поста'''
    user: UserSchema
    id: int
    timestamp: datetime
    content: str
    num_comments: int

class PostCreateSchema(Schema):
    '''Схема поста'''
    content: str