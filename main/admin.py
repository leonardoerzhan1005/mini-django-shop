from django.contrib import admin

# Register your models here.
# Создал Админку и зарегали админку
from .models import Category,Product

@admin.register(Category) # декоратор
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category',
                    'price','available']
    list_filter = ['available','created','updated','category']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}
