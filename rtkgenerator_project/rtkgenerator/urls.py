from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="rtk_app/home.html"), name='home'),
    path("admin/", admin.site.urls),
    re_path(r"^rtk/", include('rtk_app.urls')),]
    
