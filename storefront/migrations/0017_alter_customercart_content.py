# Generated by Django 4.0.3 on 2023-01-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0016_alter_customercart_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercart',
            name='content',
            field=models.CharField(choices=[('egg', 'egg'), ('eggless', 'eggless')], default='egg', max_length=35),
        ),
    ]