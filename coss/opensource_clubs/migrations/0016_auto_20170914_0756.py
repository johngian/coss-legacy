# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensource_clubs', '0015_auto_20170913_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubprofile',
            name='avatar_url',
        ),
        migrations.RemoveField(
            model_name='clubprofile',
            name='github_link',
        ),
        migrations.RemoveField(
            model_name='clubprofile',
            name='mozillian_username',
        ),
    ]
