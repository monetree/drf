# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-03 07:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serializers', '0002_auto_20181003_0400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name=b'language_logo',
        ),
    ]
