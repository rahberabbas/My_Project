from django.shortcuts import render
from django.http import HttpResponse
from .models import Context
# Create your views here.

def index(request):
    # Context.name.isUpper()
    mypr = Context.objects.all()
    return render(request,'prone/index.html',
                {'mypr':mypr})

def vid(request , myid):
    vido = Context.objects.filter(num = myid)[0]
    return render(request,'prone/vid.html',
                {'vido':vido})

# def Context(request):
#     if request.method=="POST":
#         name = request.POST.get('name' , '')
#         cat = request.POST.get('cat','')
#         desc = request.POST.get('desc','')
#         img = request.POST.get('img','')
#         vide = request.POST.get('vide', '')
#         ad = Context(nam=nam,cat=cat,desc=desc,img=img,vide=vide)
#         ad.save()
#     return render(request,'prone/add.html')
