# Generated by Django 2.2.3 on 2019-07-29 05:40

import art.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(default='', max_length=500)),
                ('image', models.ImageField(default='', upload_to=art.models.get_art_image_path)),
            ],
        ),
    ]
