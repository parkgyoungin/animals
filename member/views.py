from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'member/index.html')

def tryJoin(request):
    return HttpResponse(request.POST["ID"])
# Create your views here.