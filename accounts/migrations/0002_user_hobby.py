# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hobby',
            field=models.CharField(default='gems', max_length=256),
            preserve_default=False,
        ),
    ]
