# Generated by Django 3.2.7 on 2021-10-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20211015_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrequest',
            name='note',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
