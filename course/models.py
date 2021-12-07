from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField('title', max_length=100)
    content = models.TextField('content')
    instrument = models.CharField('instrument', max_length=30)
    level = models.CharField('level', max_length=30)
    price = models.DecimalField('price', max_digits=7, decimal_places=2, default=0.0)
    location = models.CharField('location', max_length=20)
    certification = models.CharField('certifi', max_length=30)
    create_time = models.DateTimeField('create_time', auto_now_add=True)
    update_time = models.DateTimeField('update_time', auto_now=True)
    is_active = models.BooleanField('is_active', default=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'course'




class Comment(models.Model):
    content = models.CharField('content', max_length=255)
    create_time = models.DateTimeField('create_time', auto_now_add=True)
    update_time = models.DateTimeField('update_time', auto_now=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    the_course = models.ForeignKey(Course, on_delete=models.CASCADE)



class Message(models.Model):
    title = models.CharField('title', max_length=50, default='')
    message = models.TextField('message')
    create_time = models.DateTimeField('create_time', auto_now_add=True)
    sender = models.ForeignKey('user.User', on_delete=models.CASCADE)
    the_course = models.ForeignKey(Course, on_delete=models.CASCADE)
