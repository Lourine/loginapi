from django.db import models
from django.contrib.auth.hashers import make_password


class MyUser(models.Model):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.name

    def save(self, **kwargs):
        some_salt = 'some_salt' 
        hashed_password = make_password(self.password, some_salt)
        self.password = hashed_password
        
        super().save(**kwargs)