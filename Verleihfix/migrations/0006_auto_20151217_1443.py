# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Verleihfix', '0005_auto_20151204_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_de',
            field=models.CharField(null=True, max_length=80),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(null=True, max_length=80),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thing',
            name='description_de',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='thing',
            name='description_en',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='type',
            name='description_de',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='type',
            name='description_en',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='type',
            name='name_de',
            field=models.CharField(null=True, max_length=80),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='type',
            name='name_en',
            field=models.CharField(null=True, max_length=80),
            preserve_default=True,
        ),
    ]
