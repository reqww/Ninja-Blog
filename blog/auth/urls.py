from django.urls import path
from ninja import NinjaAPI

from .views import views

api = NinjaAPI(urls_namespace='auth')

api.add_router('', views)

urlpatterns = [
    path('', api.urls)
]