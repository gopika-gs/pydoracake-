# Generated by Django 4.0.3 on 2023-02-20 06:50

import adminpannel.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys',
            name='img',
            field=models.ImageField(upload_to=adminpannel.models.get_upload_path),
        ),
    ]