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
    id = request.POST['user_id']
    is_exist =  len(Member.objects.filter(user_id=id))
    can_use = canUse(id)
    check = False
    if len(id) == 0:
        result = "아이디를 입력해주세요"
    elif is_exist:
        result = ' "{}" 는 이미 사용중인 아이디 입니다'.format(id)
    elif not can_use:
        result = "아이디는 영문(소문자), 숫자로만 구성되어야 합니다"
    else:
        result = "'{}' 는 사용 가능합니다".format(id)
        check = True

    print("id : %s, %s"%(id,result))
    context = {"check":check, "result":result}
    return render(request, "member/idCheck.html", context)

def canUse(id):
    for c in id:
        if not c.islower() and not c.isdecimal():
            return False
    return True

