from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import userform
from.models import Quizques
from django.db.models import Count
import time
# Create your views here.

def index(request):
    subjects=Quizques.objects.values('subject_name').annotate(dcount=Count('subject_name'))
    return render(request,'quizz/home.html',{'subjects':subjects})
@login_required
def special(request):
    return render(request,'quizz/home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered=False;
    if request.method=='POST':
        p=userform(data=request.POST)
        if p.is_valid():
            user=p.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(p.errors)
    else:
        p=userform()
    return render(request,'quizz/register.html',{'form':p,'registered':registered})


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("login failed")
            return HttpResponse("invalid")
    else:
        return render(request,'quizz/login.html',{})

def homecheck(request):
    subjects=Quizques.objects.values('subject_name').annotate(dcount=Count('subject_name'))
    return render(request,'home.html',{'subjects':subjects})
# Create your views here.
q_no=1
r_ans=0
w_ans=0
s_id=""
tot_ques=100

def qp(request):
    global q_no
    global s_id
    global tot_ques
    global tic
    q_no=1
    global r_ans
    r_ans=0
    global w_ans
    w_ans=0
    # qp1(request)
    if request.method=='POST':
        print("vanthuten")
        s_id=request.POST.get('q')
        print(s_id)
        temp_tot=Quizques.objects.values('subject_name').annotate(dcount=Count('subject_name'))
        for i in temp_tot:
            if i['subject_name']==s_id:
                tot_ques=i['dcount']
        tic=time.perf_counter()
        quest=Quizques.objects.filter(subject_name=s_id,question_no=q_no)
    return render(request,'quizz/quiz.html',{'question':quest})
    # return render(request,'home.html')
def qp1(request):
    global q_no
    global tic
    global r_ans
    global w_ans
    global tot_ques
    if request.method=='POST':
        ans=request.POST.get('q')
        if ans:
            q_no+=1
            an=Quizques.objects.filter(subject_name=s_id,question_no=q_no-1)
            # print(an[0].ans,"ur choice:",a)
            if ans==an[0].ans:
                r_ans+=1
            else:
                w_ans+=1
    if(q_no<=tot_ques):
        quest=Quizques.objects.filter(subject_name=s_id,question_no=q_no)
        return render(request,'quizz/quiz.html',{'question':quest})
    else:
        toc=time.perf_counter()
        total_time=toc-tic
        minu=int(total_time//60)
        hours=minu//60
        secs=round(total_time%60,2)
        if minu<=9:
            minute='0'+str(minu)
        else:
            minute=minu
        show_time='0'+str(hours)+" hours: "+str(minute)+" minutes: "+str(secs)+" seconds"
        return render(request,'quizz/result.html',{'score':r_ans,'total':show_time})
