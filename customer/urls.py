from django.urls import path
from customer.views import *
urlpatterns = [
    path('reservation/',Reservation,name='reservation'),
    path('account/',Account,name='account'),
    path('logout/',Logout,name='logout'),
    path('cart/', Cart,name='cart'),
    path('delete_order/<int:Oid>/', DeleteOrder, name='deleteOrder')
]
