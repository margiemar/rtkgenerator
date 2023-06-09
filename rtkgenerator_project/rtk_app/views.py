from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


from .forms import *
from .models import *
from .utils import *


class OrderDetails(TemplateView):
    template_name = "rtk_app/order_details.html"

def pageNotFound(request, exception):
    #with open("rtk_app/images/404.png", "rb") as img:
    #    return FileResponse(img)
    HttpResponse("ydyvcyfvyvfy")