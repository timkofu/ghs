# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitstars', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='language',
            index=models.Index(fields=['name'], name='gitstars_la_name_1db1a4_idx'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['name', 'full_name', 'description'], name='gitstars_pr_name_03fed0_idx'),
        ),
    ]