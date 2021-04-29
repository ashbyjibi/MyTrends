from django.shortcuts import render
from shopapp.models import Product
from django.db.models import Q

# Create your views here.

def searchResult(request):
    products=None
    query=None
    if 'searchme' in request.GET:
      query=request.GET.get('searchme')
      products=Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,"search.html",{'query':query,'products':products})

