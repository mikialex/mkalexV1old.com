# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPage', '0023_remove_cheet_sheet_project_project_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('describe', models.CharField(blank=True, max_length=100)),
                ('publish_time', models.DateTimeField()),
                ('content_type', models.CharField(max_length=20)),
                ('content', models.TextField(blank=True)),
                ('page_view', models.IntegerField(default=0)),
                ('has_cover', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-publish_time'],
            },
        ),
    ]
