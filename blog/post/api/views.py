from django.shortcuts import get_object_or_404
from ninja import Router

from typing import List
from asgiref.sync import sync_to_async
import asyncio

from post.models import Post, Comment
from .schemas import PostSchema, PostCreateSchema
from auth.jwt import AuthBearer

views = Router()

# @views.get('post/')
# async def get_posts(request):
#     posts = await sync_to_async(list(Post.objects.all()))()
#     return posts

@views.get('post/', response=List[PostSchema])
def get_posts(request):
    return Post.objects.all()

@views.post("post/", response=PostCreateSchema, auth=AuthBearer())
def create_post(request, post: PostCreateSchema):
    return Post.objects.create(user=request.auth, **post.dict())