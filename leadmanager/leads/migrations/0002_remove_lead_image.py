# Generated by Django 3.0.5 on 2020-07-21 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='image',
        ),
    ]
