from django.db import models

class tweet(models.Model):
    user = models.CharField(max_length=15)
    body = models.CharField(max_length=280)
    def __str__(self):
        return self.body