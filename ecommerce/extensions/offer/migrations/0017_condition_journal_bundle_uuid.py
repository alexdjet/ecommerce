# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 19:34
# TODO: journals dependency
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0016_auto_20180124_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='journal_bundle_uuid',
            field=models.UUIDField(blank=True, null=True, verbose_name='JournalBundle UUID'),
        ),
    ]
