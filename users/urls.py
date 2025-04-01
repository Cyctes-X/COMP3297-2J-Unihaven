from django.urls import path
from .views import RegisterView,LoginView, HomeView, HKU_member_view, Cedars_view, Property_owner_view
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('hku_member/', HKU_member_view.as_view(), name='hku_member'),
    path('cedars/', Cedars_view.as_view(), name='cedars'),
    path('property_owner/', Property_owner_view.as_view(), name='property_owner'),

]