# Generated by Django 3.2 on 2021-04-27 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='smalltitle',
            field=models.CharField(default='無標題', max_length=10),
        ),
    ]
