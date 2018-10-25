# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from .models import Register
from login.handler.forms import userForm,loginForm
from django.shortcuts import render_to_response

'''
Module Description

Created on Oct 20, 2018
@author: chunyan.guo
@change: Jan 20, 2018 roaddb: initialization
'''


def regist(request):
    form = userForm()
    if request.method == "POST":
        form = userForm(request.POST.copy())
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            newpassword = form.cleaned_data["newpassword"]
            phone = form.cleaned_data["phone"]
            if password != newpassword:
                return HttpResponse('重复登录密码与登录密码不一致');
            reg = Register.objects.create(email=email, password=password, phone=phone)
            reg.save()
            return render_to_response('login/registe_ok.html', {'form': form});
    return render_to_response('login/register.html', {'form': form});


# 用户登录
def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST.copy())
        if form.is_valid():
            human = True
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Register.objects.filter(email__exact=email, password__exact=password)
            if user:
                #start session to record user info for index
                request.session['email'] = email
                return HttpResponseRedirect('/index/')   #login success
            else:
                return HttpResponseRedirect('/login/')  #login fail

    else:
        form = loginForm()
        if request.GET.get('newsn') == '1':
            csn = CaptchaStore.generate_key()
            cimageurl = captcha_image_url(csn)
            return HttpResponse(cimageurl)
    return render_to_response('login/login.html', {'form': form});

def index(request):

    email =request.session.get('email')
    return  render_to_response('login/index.html',{'email': email});


def logout(request):
    pass