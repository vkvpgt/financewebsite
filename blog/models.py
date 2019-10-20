from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customername = models.CharField(max_length=200)
    amount =  models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.customername

class Update(models.Model):
    
    token = models.IntegerField()
    givenamount = models.CharField(max_length=200)
    given_date = models.DateTimeField(default=timezone.now)

   
    def __str__(self):
        return self.givenamount