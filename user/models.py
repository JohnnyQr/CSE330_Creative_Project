from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField('username', max_length=30, unique=True)
    password = models.CharField('password', max_length=255)
    create_time = models.DateTimeField('create_time', auto_now_add=True)
    update_time = models.DateTimeField('update_time', auto_now=True)


    def __str__(self):
        return 'username %s' % self.username
    

