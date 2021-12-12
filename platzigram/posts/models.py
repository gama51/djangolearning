from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):

    uuid = models.UUIDField()

    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)

    country=models.CharField(max_length=50,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    is_admin=models.BooleanField(default=False)

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    bio=models.TextField(blank=True)
    birthdate=models.DateField(blank=True,null=True)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.email+':'+self.city+':'+self.country)
    
class Post(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey('users.Profile',on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    photo =models.ImageField(upload_to='posts/photos')
    created =models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '{} by @{}'.format(self.title, self.user.username)