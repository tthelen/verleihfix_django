# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Verleihfix', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lending',
            name='duration',
        ),
        migrations.AddField(
            model_name='lending',
            name='end',
            field=models.DateField(default=datetime.datetime(2015, 10, 26, 12, 46, 28, 90190, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
