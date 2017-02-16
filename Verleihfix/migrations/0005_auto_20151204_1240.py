# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Verleihfix', '0004_auto_20151202_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='home', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lending',
            name='status',
            field=models.CharField(max_length=1, choices=[('r', 'Reserviert'), ('l', 'Ausgeliehen'), ('x', 'Zurückgegeben'), ('o', 'Storniert')]),
            preserve_default=True,
        ),
    ]
