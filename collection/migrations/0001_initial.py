# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 18:27
from __future__ import unicode_literals

import collection.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Collectible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=collection.models.image_upload_handler)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('creator', models.CharField(max_length=128)),
                ('artist', models.CharField(blank=True, max_length=128, null=True)),
                ('publisher', models.CharField(blank=True, max_length=128, null=True)),
                ('pubyear', models.DateTimeField(auto_now_add=True, null=True)),
                ('copyright', models.DateTimeField(auto_now_add=True, null=True)),
                ('identifier', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('classification', models.ManyToManyField(related_name='collectibles', to='collection.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PRIV', 'Private'), ('PUBL', 'Public')], max_length=4)),
                ('image', models.ImageField(upload_to=collection.models.image_upload_handler)),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=128)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='collections', to='collection.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('link', models.FileField(blank=True, null=True, upload_to='')),
                ('collectible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='collection.Collectible')),
            ],
        ),
        migrations.AddField(
            model_name='collectible',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='collection.Collection'),
        ),
    ]
