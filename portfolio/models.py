from django.db import models
from django import forms
from django.utils import timezone 
from django.contrib.auth.models import User

def user_path(instance, filename):
    from random import choice
    import string 
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1] 
    return '%s/%s.%s' % (instance.owner.username, pid, extension) 

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length=500)
    idname = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self): 
        return self.title
        return '%s by %s' % (self.title, self.idname) 

    def summary(self):
        return self.description[:100]
    
