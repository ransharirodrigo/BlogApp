from django.db import models

from users.models import CustomUser

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field='email',default=None)