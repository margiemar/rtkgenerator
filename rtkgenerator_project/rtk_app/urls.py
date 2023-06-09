from django.urls import path, re_path, include
from .views import *


urlpatterns = [
    path('orderdetails/', OrderDetails.as_view(), name='orderdetails'),
]

urlpatterns += [
    path('onetimework/', CreateOneTimeWorkView.as_view(), name='onetimework'),
    path('userorder/', CreateUserOrderView.as_view(), name='userorder'),
]