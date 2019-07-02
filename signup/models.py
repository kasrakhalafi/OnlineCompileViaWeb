from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username
