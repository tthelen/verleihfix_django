# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Verleihfix', '0006_auto_20151217_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_fr',
            field=models.CharField(max_length=80, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thing',
            name='description_fr',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='type',
            name='description_fr',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='type',
            name='name_fr',
            field=models.CharField(max_length=80, null=True),
            preserve_default=True,
        ),
    ]
