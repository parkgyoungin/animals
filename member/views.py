from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django import forms
def index(request):
    return render(request,'member/index.html')

def tryJoin(request):
    #print(request.POST)
    #member = Member.objects.all() #member[row].colum

    #member = Member(name=request.POST['name'], user_id=request.POST['user_id'], password=request.POST['password']
    #                , phone_number=request.POST['phone_number'] , gender=request.POST['gender'] , animal_count=request.POST['animal_count'])
    #member.save()
    #member = Member.objects.filter(name='박경민')
    idCheck = len(Member.objects.filter(user_id=request.POST['user_id']))
    if idCheck:
        print("저장불가")
    else:
        print("저장가능")



    return HttpResponse("oo")
# Create your views here.

def idCheck(request):
    return render(request, "member/idCheck.html")
