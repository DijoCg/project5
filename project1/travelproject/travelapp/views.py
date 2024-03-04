from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from .models import Team

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    team = Team.objects.all()
    return render(request,'index.html',{'result':obj,'ref':team})