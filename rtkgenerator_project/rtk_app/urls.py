from django.urls import path, re_path, include
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path('orderdetails/', OrderDetails.as_view(), name='orderdetails'),
    path("contacts/", TemplateView.as_view(template_name="rtk_app/contacts.html")),

]

urlpatterns += [
    path('onetimework/', CreateOneTimeWorkView.as_view(), name='onetimework'),
    path('userorder/', CreateUserOrderView.as_view(), name='userorder'),
]