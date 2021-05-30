# Generated by Django 3.2.3 on 2021-05-30 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unnamed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='bio',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
