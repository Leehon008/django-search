from django.urls import path
from Cities.views import *

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('search/', CitySearches.as_view(), name='search'),
    path('cities/', AllCities.as_view(), name='cities'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Register.as_view(), name='register'),
]
