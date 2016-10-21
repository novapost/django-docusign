# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-05 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_docusign_demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signer',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='signer',
            name='signing_order',
            field=models.PositiveSmallIntegerField(default=0, help_text='Position in the list of signers.', verbose_name='signing order'),
        ),
    ]