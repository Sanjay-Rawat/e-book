# Generated by Django 3.2.5 on 2021-07-29 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('about', models.TextField(max_length=1000)),
                ('fileUrl', models.TextField(max_length=1000)),
                ('category', models.CharField(max_length=50)),
                ('isForMembers', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
