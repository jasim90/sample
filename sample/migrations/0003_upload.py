# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 03:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_auto_20160328_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(code='invalid_file_name', message='File name must be Alphanumerics', regex='^[a-zA-Z0-9]*$')])),
                ('file', models.FileField(upload_to=b'')),
            ],
        ),
    ]
