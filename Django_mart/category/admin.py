from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdminRegister(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('category_name', )}
    list_display = ['category_name', "slug", 'description',]
admin.site.register(Category, CategoryAdminRegister)