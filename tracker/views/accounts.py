from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .. models import *
from .. serializers import *


@login_required
def index(request):
    projects = ProjectMaster.objects.all()
    return render(request,'tracker/index.html',{"projects":projects})

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            return render(request,'registration/login.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)