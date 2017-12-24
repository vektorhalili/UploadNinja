from django.db import models
from django.forms import ModelForm
from upload.forms import *


# Create your models here.
class Files(models.Model):
    name = models.CharField(max_length=100)
    location = models.FileField(upload_to='files/')
    def __str__(self):
        return self.name


class FileForm(ModelForm):
    class Meta:
        model = Files
        fields = ['name','location']
