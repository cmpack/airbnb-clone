# Generated by Django 2.2.5 on 2021-01-03 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_auto_20201231_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
    ]
