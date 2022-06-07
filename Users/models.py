from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms import ModelForm

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='pictures/default.jpg', upload_to="pictures")
    
    def __str__(self):
        return f"{self.user.username} profile"

