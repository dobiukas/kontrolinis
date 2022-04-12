from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
#from orders.models import Order, User, Product

@login_required(login_url='login')
@admin_only
def home(request):
    breakfast=Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:5]
    lunch=Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5]
    dinner=Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5]
    snacks=Category.objects.filter(name='snacks')[0].fooditem_set.all()[:5]
    customers=Customer.objects.all()
    context={'breakfast':breakfast,
              'lunch':lunch,
              'dinner':dinner,
              'snacks':snacks,
              'customers':customers,
            }
    return render(request,'main.html',context)



