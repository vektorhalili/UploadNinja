# Generated by Django 2.0 on 2017-12-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20171224_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
