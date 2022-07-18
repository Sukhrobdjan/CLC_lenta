from django.db import models
from helpers.models import BaseModel
from lenta.models import Commentary




class User(BaseModel):
    name = models.CharField(max_length=500)
    founded_at = models.CharField(max_length=500)
    username = models.CharField(max_length=50)
    describe = models.TextField(null = True)
    email = models.EmailField()
    fb_link = models.CharField(max_length=100)
    insta_link = models.CharField(max_length=100)
    imkon_link = models.CharField(max_length=100)
    pochta_link = models.CharField(max_length=100)
    telegram_link = models.CharField(max_length=100)
    site_link = models.CharField(max_length=100)



class Author(BaseModel):
    name = models.CharField(max_length=70)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Range(BaseModel):
    title = models.CharField(max_length=200)
    describe = models.TextField()


class Tag(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
