from django.urls import path, include
from .views import index, getPhoto, addPhoto

urlpatterns = [
    path('', index, name='index'),
    path('photo/<int:id>/', getPhoto, name="getPhoto"),
    path('add', addPhoto, name="addPhoto")

]