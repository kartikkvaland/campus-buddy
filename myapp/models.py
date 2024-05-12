from django.db import models

# Create your models here.
class User(models.Model):

    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    otp=models.IntegerField(default=1234)

    def __str__(self):
        return self.name
    

class Media(models.Model):

    video=models.FileField(upload_to='media/video')
   
