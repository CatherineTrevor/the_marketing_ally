# Generated by Django 3.2.7 on 2021-10-04 11:39

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20210924_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quoterequest',
            old_name='date',
            new_name='request_date',
        ),
        migrations.RemoveField(
            model_name='quoterequest',
            name='quote_request_id',
        ),
        migrations.AddField(
            model_name='quoterequest',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quoterequest',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='quoterequest',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Phone number', max_length=31),
        ),
        migrations.AlterField(
            model_name='quoterequest',
            name='consultation_status',
            field=models.CharField(blank=True, choices=[('1', 'Update consultation status'), ('2', 'No consultation requested'), ('3', 'Consultation requested'), ('4', 'Consultation booked')], default=1, max_length=254),
        ),
    ]