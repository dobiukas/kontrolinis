from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.

class food(admin.ModelAdmin):
    class Meta:
        model = Food
    list_display = ['name']
    list_filter = ['name']




admin.site.register(Customer)
admin.site.register(UserFood)
admin.site.register(Category)
admin.site.register(Food, food)
