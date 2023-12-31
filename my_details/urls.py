from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', upstox_login, name='upstox_login'),
    path('upstox/callback', get_access_token,name='get_access_token'),
    path('get_user_profile/', get_user_profile, name='get_user_profile'),
    path('get_orders/', get_orders, name='get_orders'),
    path('each_order/<int:id>/',each_order,name='each_order'),
] 


#  upstox_redirect