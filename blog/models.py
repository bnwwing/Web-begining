from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=40,default='Title')
    content=models.TextField(null=True)
    pub_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Login(models.Model):
    username=models.CharField(max_length=30,default='')
    password=models.CharField(max_length=40,default='')