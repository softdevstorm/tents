# Generated by Django 2.2.3 on 2019-07-12 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AlterModelTable(
            name='photo',
            table='gallery_photo',
        ),
    ]
