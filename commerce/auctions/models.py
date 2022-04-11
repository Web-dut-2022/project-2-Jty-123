from django.contrib.auth.models import AbstractUser
from django.db import models

"""
用户模型
"""
class User(AbstractUser):
    pass
    # #用户名
    # userName = models.CharField('用户名', primary_key=True, max_length=64)
    # #邮箱
    # userEmail =models.CharField('邮箱', max_length=64)
    # #密码
    # userPassword =models.CharField('密码', max_length=64)