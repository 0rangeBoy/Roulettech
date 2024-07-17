from django.db import models

# Create your models here.


class PersonalAppText(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=120)
    def _str_(self):
        return self.title
    
class PersonalAppImg(models.Model):
    title = models.CharField(max_length=20)
    imgURL = models.CharField(max_length=300)
    def _str_(self):
        return self.title