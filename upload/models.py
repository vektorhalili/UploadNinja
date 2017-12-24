from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=100),
    size = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    downloads = models.IntegerField()
    description = models.CharField(max_length = 255)
    location = models.FileField(upload_to='files/')
    def __str__(self):
        return self.name
