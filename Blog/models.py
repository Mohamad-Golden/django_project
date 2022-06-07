from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import pytz
from django.urls import reverse_lazy


def timenow():
    return datetime.now(tz=pytz.timezone('Asia/Tehran'))

class Post(models.Model):
    ch = [('p10', "post 10"), ("p11", "post 11")]
    title = models.CharField(max_length=20, choices=ch)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timenow, help_text="تاریخ الان")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse_lazy('blog-post', kwargs={'pk':self.pk})