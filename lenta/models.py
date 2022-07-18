from django.db import models
from helpers.models import BaseModel
from authors.models import User,Author


OMMABOP = "ommabop"
SUNGILARI = "so`ninglari"
POST_STATUS = (
    (OMMABOP, "created"),
    (SUNGILARI, "moderation"),
)


BARCHASI = "barchasi"
PREMIUM = "premium"
PINDAGILAR = "pindagilar"
TADBIR_STATUS = (
    (BARCHASI, "barchasi"),
    (PREMIUM, "premium"),
    (PINDAGILAR, "pindagilar"),
)


class Company(BaseModel):
    name = models.CharField(max_length=500)
    description = models.TextField()
    tag_name = models.CharField(max_length=50,null = True)
    founded_at = models.BigIntegerField(default=0)
    followers = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    followers = models.ForeignKey(Author,on_delete=models.CASCADE,null = True)
    icon = models.ImageField(upload_to = 'company_icon/')
    image = models.ImageField(upload_to = 'company_img/')


class Category(BaseModel):
    title = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    icon = models.FileField(upload_to="category/")
    # post_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'cate_image/')
    follwers = models.ForeignKey('Author',on_delete=models.CASCADE,null = True)

    

class Commentary(models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to = 'comment_photo/')
    comment = models.ForeignKey(User,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)





class Post(BaseModel):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    views = models.BigIntegerField(default=0)

    category = models.ForeignKey(on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=POST_STATUS)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(Company,on_delete = models.CASCADE)
    status = models.CharField(max_length=15, choices=POST_STATUS)
    commentary = models.ForeignKey()
    


class Tadbir(BaseModel):
    title = models.CharField(max_length=500)
    description = models.TextField()
    slug = models.SlugField(max_length=100,unique=True)

    icon = models.ImageField(upload_to = 'icon/')
    image = models.ImageField(upload_to = 'tadbir_img/')

    status = models.CharField(max_length=15, choices=TADBIR_STATUS)








class Vacancy(BaseModel):
    title = models.CharField(max_length=500)
    description = models.TextField()
    slug = models.SlugField(max_length=100,unique=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    tasks = models.TextField()
    sharoit = models.TextField()
    salary = models.BigIntegerField(default=0)
