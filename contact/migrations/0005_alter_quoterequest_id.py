# Generated by Django 3.2.7 on 2021-10-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_quoterequest_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoterequest',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]