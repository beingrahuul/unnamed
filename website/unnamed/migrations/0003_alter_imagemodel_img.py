# Generated by Django 3.2.3 on 2021-06-04 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unnamed', '0002_auto_20210604_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]