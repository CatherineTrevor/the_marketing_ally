# Generated by Django 3.2.7 on 2021-10-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_quoterequest_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoterequest',
            name='id',
            field=models.BigAutoField(default='1', primary_key=True, serialize=False),
        ),
    ]
