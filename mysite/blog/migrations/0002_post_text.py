# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-27 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='Content coming soon.'),
        ),
    ]
