# Generated by Django 4.0.3 on 2023-02-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(default='', max_length=50)),
                ('flavour', models.CharField(default='chocolate', max_length=100)),
                ('price', models.IntegerField()),
                ('shape', models.CharField(max_length=50)),
                ('size', models.IntegerField(default='6')),
                ('stock', models.CharField(choices=[('Stock Available', 'Stock Available'), ('Out of stock', 'Out of stock')], default='Stock Available', max_length=30)),
            ],
        ),
    ]