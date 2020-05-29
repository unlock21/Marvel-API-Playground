from django.db import models

class Character(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=10000)
    def __str__(self):
        return self.name

class Comic(models.Model):
    name = models.CharField(max_length=500)
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.name