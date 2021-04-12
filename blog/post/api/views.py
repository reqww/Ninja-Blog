from django.shortcuts import get_object_or_404
from django.db.models import Count
from ninja import Router

from typing import List
from asgiref.sync import sync_to_async

from post.models import Post, Comment
from .schemas import PostSchema, PostCreateSchema
from auth.jwt import AuthBearer

views = Router()

async def get_queryset():
    posts = Post.objects.all()
    return posts.annotate(num_comments=Count('comments'))

@views.get('post/{pk}/', response=PostSchema)
async def get_posts(request, pk: int):
    posts = await get_queryset()
    return await sync_to_async(posts.get)(pk=pk)
    
@views.get('post/', response=List[PostSchema])
async def get_posts(request):
    return await get_queryset()

@views.post("post/", response=PostCreateSchema, auth=AuthBearer())
def create_post(request, post: PostCreateSchema):
    return Post.objects.create(user=request.auth, **post.dict())