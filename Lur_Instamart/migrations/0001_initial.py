# Generated by Django 4.2.5 on 2023-10-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOKS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_image', models.CharField(max_length=1000)),
                ('book_title', models.CharField(max_length=1000)),
                ('author_name', models.CharField(max_length=1000)),
                ('publish', models.CharField(max_length=1000)),
                ('disc', models.CharField(max_length=1000)),
            ],
        ),
    ]
