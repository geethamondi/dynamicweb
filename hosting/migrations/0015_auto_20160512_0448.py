# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 04:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0014_auto_20160505_0541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostingorder',
            old_name='VMPlan',
            new_name='vm_plan',
        ),
    ]
