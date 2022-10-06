from django.db import models

# Create your models here.
class Adv(models.Model):
    title=models.CharField(max_length=25)
    decription=models.TextField(max_length=255)


    def __str__(self) :
        return self.title    