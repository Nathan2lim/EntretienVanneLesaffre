from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class VanneUser(User):
    num = models.IntegerField()