from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=255)

class wheel(models.Model):
    # 图片
    img = models.CharField(max_length=100)
    # 名称
    name = models.CharField(max_length=100)
    # 商品编号
    trackid = models.CharField(max_length=10)
