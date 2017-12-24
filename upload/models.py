from django.db import models
from django.forms import ModelForm
from upload.forms import *
import os
import itertools
from django.utils.text import slugify

# Create your models here.
class File(models.Model):
    location = models.FileField(upload_to='files/')
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.location.name
    @models.permalink
    def get_absolute_url(self):
        return 'upload:file', (self.slug,)
#    @property
#    def relative_path(self):
#        return os.path.relpath(self.location)


class FileForm(ModelForm):
    location = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = File
        fields = ['location']
    def save(self):
        instance = super(FileForm, self).save(commit=False)
        instance.slug = slugify(instance.location.name)
        for x in itertools.count(1):
            if not File.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)
        instance.save()
        return instance
