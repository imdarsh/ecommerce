from django.shortcuts import render

from . models import Product
# Create your views here.
def index(request):
    data = Product.objects.all()
    return render(request,'index.html',{'products':data})

def contact(request):
    return render(request,'contact.html')