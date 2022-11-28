from django.shortcuts import render, redirect
from django.contrib.auth import hashers
from django.http import HttpResponseNotFound, JsonResponse
import re
from .forms import *
from .models import *


def reg_user(request):
    if request.session.get("login") is not None:
        return redirect('/')
    if request.method == "GET":
        regForm = RegForm
        return render(request, "reg.html", {"form": regForm})
    elif request.method == "POST":
        user = UserModel
        user.name = request.POST.get("name")
        user.login = request.POST.get("login")
        user.password = hashers.make_password(request.POST.get("password"))
        rep_password = request.POST.get("rep_password")
        user.email = request.POST.get("email")
        user.role = 1 # По умолчанию задаём роль - 1, то есть обычный пользователь
        if hashers.check_password(user.password, rep_password):
            return HttpResponseNotFound('<h3 style="color:red">Пароли должны совпадать!</h3>')
        if re.search('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', user.email) is None:
            return HttpResponseNotFound('<h3 style="color:red">ВАша электронная почта некорректна!</h3>')
        user.save()
        request.session['login'] = user.login
        return redirect("/")


def login(request):
    if request.session.get("login") is not None:
        return redirect('/')
    if request.method == "GET":
        logForm = LoginForm
        return render(request, "login.html", {"form": logForm})
    elif request.method == "POST":
        log = request.POST.get("login")
        password = request.POST.get("password")
        try:
            user = UserModel.objects.get(login=log)
        except BaseException:
            return HttpResponseNotFound('<h3 style="color:red">Такого пользователя не существует</h3>')
        if hashers.check_password(password, user.password):
            request.session['login'] = log
            return redirect("/")
        else:
            return HttpResponseNotFound('<h3 style="color:red">Введён неверный логин или пароль!</h3>')


def logout(request):
    try:
        del request.session['login']
    except KeyError:
        pass
    return redirect("/")

def validate_login(request):
    login = request.GET.get('login', None)
    response = {
        'is_taken': UserModel.objects.filter(login=login).exists()
    }
    return JsonResponse(response)

def validate_email(request):
    email = request.GET.get('email', None)
    response = {
        'is_taken': UserModel.objects.filter(email=email).exists()
    }
    return JsonResponse(response)
