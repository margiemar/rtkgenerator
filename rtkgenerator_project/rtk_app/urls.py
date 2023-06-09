from django.urls import path, re_path, include
from .views import *


urlpatterns = [
    path('orderdetails/', OrderDetails.as_view(), name='orderdetails'),
]

