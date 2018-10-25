#!/usr/bin/env python
# encoding: utf-8

from login.models import Register
from django import forms
'''
Module Description

Created on Oct 20, 2018
@author: chunyan.guo
@change: Jan 20, 2018 roaddb: initialization
'''


class userForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    newpassword = forms.CharField()
    phone = forms.CharField()

    def clean(self):
        cleaned_data = super(userForm, self).clean()
        password = cleaned_data.get("password")
        newpassword = cleaned_data.get("newpassword")
        if password and newpassword:
            if password != newpassword:
                msg = u"两个密码字段不一致。"
                print msg
        return cleaned_data

    def clean_email(self):
        '''''验证重复email'''
        emails = Register.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError(u"该邮箱已经被使用请使用其他的")


class loginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    def clean_email(self):
        '''''验证重复email'''
        emails = Register.objects.filter(email__iexact=self.cleaned_data["email"])
        if emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError(u"该邮箱没有注册，请注册！")

    def clean_password(self):
        '''''验证密码是否正确'''
        password = Register.objects.filter(password__iexact=self.cleaned_data["password"])
        if password:
            return self.cleaned_data["password"]
        raise forms.ValidationError(u"密码错误！")

