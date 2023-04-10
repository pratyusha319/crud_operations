from django.shortcuts import render
from app.models import *
# Create your views here.
def display_customer(request):
    Qsc=Customer.objects.all()
    d={'customers':Qsc}
    return render(request,'display_customer.html',d)
def display_orders(request):
    Qso=Orders.objects.all()
    d={'orders':Qso}
    return render(request,'display_orders.html',d)
def display_order_details(request):
    Qsod=Orderdetails.objects.all()
    d={'orderdetails':Qsod}
    return render(request,'display_order_details.html',d)