# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-03 05:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0030_userhostingkey_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='virtualmachinetype',
            name='hosting_company',
        ),
        migrations.RemoveField(
            model_name='virtualmachinetype',
            name='location',
        ),
    ]