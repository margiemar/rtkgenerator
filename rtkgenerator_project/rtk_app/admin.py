from django.contrib import admin
from .models import *

class AbonReestrAdmin(admin.ModelAdmin):
    list_display = ()


class ASOCatalogAdmin(admin.ModelAdmin):
    pass

class OneTimeWorkAdmin(admin.ModelAdmin):
    pass

admin.site.register(AbonReestr, AbonReestrAdmin)
admin.site.register(ASOCatalog, ASOCatalogAdmin)
admin.site.register(OneTimeWork, OneTimeWorkAdmin)





















#class WomenAdmin(admin.ModelAdmin):
#    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
#    list_display_links = ('id', 'title')
#    search_fields = ('title', 'content')
#    list_editable = ('is_published',)
#    list_filter = ('is_published', 'time_create')
#    prepopulated_fields = {"slug": ("title",)}
#
#class CategoryAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name')
#    list_display_links = ('id', 'name')
#    search_fields = ('name',)
#    prepopulated_fields = {"slug": ("name",)}
#
#
#admin.site.register(Women, WomenAdmin)
#admin.site.register(Category, CategoryAdmin)