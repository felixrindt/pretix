# Generated by Django 2.2 on 2019-05-09 06:54

import django.db.models.deletion
import jsonfallback.fields
from django.db import migrations, models

import pretix.base.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0118_auto_20190423_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hidden',
            field=models.BooleanField(default=False, help_text='This question will only show up in the backend.', verbose_name='Hidden question'),
        ),
    ]
