from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    content = models.CharField(max_length=124)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

