# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 22:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import s3direct.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(blank=True, max_length=9, null=True)),
                ('photo', s3direct.fields.S3DirectField(blank=True, null=True)),
                ('created_on', models.DateTimeField(blank=True)),
                ('modify_on', models.DateTimeField(blank=True)),
                ('level', models.PositiveIntegerField(blank=True, default=0)),
                ('score', models.PositiveIntegerField(blank=True, default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userProfile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil de usuario',
            },
        ),
    ]
