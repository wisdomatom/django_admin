# Generated by Django 2.0.7 on 2018-07-06 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='auth_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
