# Generated by Django 4.2 on 2023-09-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]