# Generated by Django 2.0.4 on 2018-04-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]