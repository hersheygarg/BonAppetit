from django.urls import path
from .views import *

urlpatterns = [
    path('about/',About, name='about'),
    path('menu/', Menu, name='menu'),
    path('contact/', Contact, name='contact'),
    path('shop/<int:dishid>/',Shop, name='shop'),
    path('AdminHome/', AdminHome, name='AdminHome'),
    path('EditCat/', EditCategory, name='EditCat'),
    path('editdish',EditDish, name='editdish'),
    path('editteam/', editTeam, name='editteam')
]
