# Generated by Django 5.1.5 on 2025-01-22 17:43

import core.utils.app_contants
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemuser',
            name='created_on',
            field=models.BigIntegerField(default=core.utils.app_contants.default_created_on),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='phone_number',
            field=models.CharField(default=918282831229, max_length=15, unique=True),
            preserve_default=False,
        ),
    ]