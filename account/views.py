from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from . import forms
from account.models import Signup

# Create your views here.
def index(request):
    return HttpResponse("Hello there")

def form_view(request):
    form = forms.FormName()
    if request.method =="POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            a = form.cleaned_data["password"]
            b = form.cleaned_data["verify_password"]
            if a == b:
                post = form.save(commit=False)
                post.save()
            else:
                form = forms.FormName()
                return HttpResponse("Password not matched, try again")
            return redirect('/', pk=post.pk)
    else:
        form = forms.FormName()

    return render(request,'account/signup.html',{'form2':form})

def login_view(request):
    form = forms.LoginName()
    if request.method =="POST":
        form = forms.LoginName(request.POST)
        if form.is_valid():
            a = form.cleaned_data["name"]
            b = form.cleaned_data["password"]
            try:
                bb = Signup.objects.values_list('password', flat=True).get(name=a)
            except Signup.DoesNotExist:
                bb = "kjdasjhgjggjdsadbejkhsndsadasdsad"
            if b == bb:
                return HttpResponse('Hello '+ a)
            else:
                return HttpResponse('Invalid User or password')
        else:
             form = forms.LoginName()
          #      return HttpResponse("Password not matched, try again")
        return redirect('/', pk=post.pk)
    else:
        form = forms.LoginName()

    return render(request,'account/login.html',{'form3':form})