# Generated by Django 2.1.1 on 2018-09-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=30)),
                ('temperature', models.CharField(max_length=30)),
                ('humidity', models.CharField(max_length=30)),
                ('pressure', models.CharField(max_length=30)),
                ('air_quality', models.CharField(max_length=30)),
                ('decibel', models.CharField(max_length=30)),
            ],
        ),
    ]
