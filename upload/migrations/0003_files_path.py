# Generated by Django 2.0 on 2017-12-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20171224_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='path',
            field=models.FilePathField(default='files/'),
        ),
    ]