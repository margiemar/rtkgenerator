from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
import pandas as pd
import xlwt
from .models import *


from .forms import *
from .models import *
from .utils import *


class OrderDetails(TemplateView):
    template_name = "rtk_app/order_details.html"


class OrderGen(View):
    pass
#	template_name = "rtk_app/order_details.html"
#	form_class = PlayerForm
#
#	#def get(self, request, *args, **kwargs):
#	#	form = self.form_class
#	#	return render(request, self.template_name, {'form': form})
#
#	def post(self, request, *args, **kwargs):
#		form = self.form_class(request.POST)
#		if form.is_valid():
#			form.save()
#		return redirect("main:home")


def pageNotFound(request, exception):
    #with open("rtk_app/images/404.png", "rb") as img:
    #    return FileResponse(img)
    HttpResponse("ydyvcyfvyvfy")



#Поля для ввода данных

class CreateOneTimeWorkView(CreateView):
    model = OneTimeWork
    form_class = OneTimeWorkForm
    template_name = 'rtk_app/BD/bd_one_time_work.html'
    success_url = reverse_lazy('home')

class CreateUserOrderView(CreateView):
    model = UserOrder
    form_class = UserOrderForm
    template_name = 'rtk_app/BD/bd_user_order.html'
    success_url = reverse_lazy('home')    


def tabel_view(request):
    return render(request, "new.html")

def to_exel(request):
    url = "http://127.0.0.1:8000/rtk/exel/"
    #table = pd.read_html(url)[0]
    table = pd.read_html(url)
    print(table)
    #table.to_excel("test_html_to_exel.xlsx")
    return redirect('home')