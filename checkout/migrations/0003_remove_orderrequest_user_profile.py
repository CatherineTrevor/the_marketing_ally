# Generated by Django 3.2.7 on 2021-10-11 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20211011_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderrequest',
            name='user_profile',
        ),
    ]
