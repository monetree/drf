# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-04 04:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serializers', '0003_remove_language_language_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='language', to='serializers.Company'),
        ),
    ]