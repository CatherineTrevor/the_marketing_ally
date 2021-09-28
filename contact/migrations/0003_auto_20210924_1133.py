# Generated by Django 3.2.7 on 2021-09-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20210924_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoterequest',
            name='id',
        ),
        migrations.AddField(
            model_name='quoterequest',
            name='quote_request_id',
            field=models.CharField(default=False, editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='quoterequest',
            name='status',
            field=models.CharField(default='Requested', max_length=254),
        ),
    ]