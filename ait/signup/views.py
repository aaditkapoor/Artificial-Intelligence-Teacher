from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from .models import UserModel

def register(request):
    username = request.GET.get("username", "")
    email = request.GET.get("email","")

    if username or email:
        if UserModel.objects.filter(username=username).exists():
            return HttpResponse("<h2>User exists!</h2>")
        else:
            UserModel.objects.create(username=username, email=email)
            request.session['name_been_put'] = True
            request.session['username'] = username
            request.session['email'] = email
            return HttpResponseRedirect("/")

        
def login(request):
    username = request.GET.get("username", "")
    email = request.GET.get("email","")

    if username or email:
        if UserModel.objects.filter(username=username).exists():
            request.session['name_been_put'] = True
            request.session['username'] = username
            request.session['email'] = email
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("<h2>Wrong username/password</h2>")
    else:
        return HttpResponse("<h2>Empty</h2>")
        
def guest_mode(request):
    if request.GET.get("email"):
        request.session['name_been_put'] = True
        request.session['username'] = "guest"
        request.session['email'] = request.GET.get('email')
        return HttpResponseRedirect("/")
    else:
        return HttpResponse("email field empty!!")