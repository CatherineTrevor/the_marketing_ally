# Generated by Django 3.2.7 on 2021-09-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('free_consultation_request', models.BooleanField(default=False)),
                ('project_name', models.CharField(max_length=254)),
                ('project_description', models.CharField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
