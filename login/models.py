# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Register(models.Model):
    email=models.EmailField(verbose_name="电子邮箱")
    password=models.CharField(max_length=50,verbose_name="密码")
    phone= models.CharField(max_length=50, verbose_name="联系电话")

