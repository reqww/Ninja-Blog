from django.shortcuts import get_object_or_404
from ninja import Router

from typing import List

from post.models import Post, Comment
from .schemas import PostSchema

views = Router()

@views.get('/post/', response=List[PostSchema])
def get_posts(self, request):
    return Post.objects.all()