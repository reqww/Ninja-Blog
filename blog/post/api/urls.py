from django.urls import path
from ninja import NinjaAPI

from .views import views

api = NinjaAPI(urls_namespace='post')

api.add_router('', views)

urlpatterns = [
    path('', api.urls)
]