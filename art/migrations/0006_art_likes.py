# Generated by Django 2.2.3 on 2019-07-31 05:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art', '0005_auto_20190731_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
