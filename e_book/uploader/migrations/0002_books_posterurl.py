# Generated by Django 3.2.5 on 2021-07-29 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='posterUrl',
            field=models.TextField(default='True', max_length=1000),
        ),
    ]