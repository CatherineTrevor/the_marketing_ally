# Generated by Django 3.2.7 on 2021-09-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='max_hours',
            new_name='max_time_multiplier',
        ),
        migrations.AddField(
            model_name='category',
            name='is_available_guest_user',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='time_allocation_mins',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(default='Project Hours', max_length=254),
        ),
    ]