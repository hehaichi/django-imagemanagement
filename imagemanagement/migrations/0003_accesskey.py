# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('imagemanagement', '0002_auto_20170311_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessKey',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('accessKey', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]