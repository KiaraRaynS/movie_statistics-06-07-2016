# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 11:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movierating', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movieid',
            new_name='movie_id',
        ),
    ]