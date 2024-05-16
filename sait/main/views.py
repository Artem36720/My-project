from django.shortcuts import render
from django.http import HttpResponse
from .models import Tovar

def index(request):
    tovarka = Tovar.objects.all()
    content = {'tovarik': tovarka}
    return render(request,'main/sport.html',content)

def Inkup(request,my_id):
    Tovari = Tovar.objects.get(id=my_id)
    context = {'Tovari': Tovari}
    return render(request, 'main/tovar.html',context)