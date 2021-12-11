from django.db import models

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
    

