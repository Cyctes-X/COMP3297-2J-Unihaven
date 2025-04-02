from django.urls import path
from .views import Home, Detail, Favorite, Contact, ListAll


urlpatterns = [

    path('Acc_Home/', Home.as_view(), name='Home'),
    path('Acc_Detail/', Detail.as_view(), name='Detail'),
    path('Acc_Favorite/', Favorite.as_view(), name='Favorite'),
    path('Acc_Contact/', Contact.as_view(), name='Contact'),
    path('Acc_ListAll/', ListAll.as_view(), name='ListAll'),

]