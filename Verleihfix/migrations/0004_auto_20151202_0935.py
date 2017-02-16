# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Verleihfix', '0003_auto_20151202_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lending',
            name='status',
            field=models.CharField(choices=[('r', 'reserved'), ('l', 'lended'), ('x', 'returned')], max_length=1),
            preserve_default=True,
        ),
    ]
