# Generated by Django 2.2.3 on 2019-08-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0008_auto_20190731_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='category',
            field=models.CharField(choices=[('fa', 'Fashion'), ('sc', 'Sculpture'), ('cr', 'Craft'), ('et', 'Etc'), ('pa', 'Painting')], default='et', max_length=2),
        ),
    ]
