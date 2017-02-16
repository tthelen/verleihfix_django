# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Verleihfix', '0002_auto_20151026_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('min_lending_span', models.IntegerField()),
                ('max_lending_span', models.IntegerField()),
                ('category', models.ForeignKey(to='Verleihfix.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='thing',
            name='category',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='image',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='max_lending_span',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='min_lending_span',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='name',
        ),
        migrations.AddField(
            model_name='thing',
            name='type',
            field=models.ForeignKey(to='Verleihfix.Type', default=2),
            preserve_default=False,
        ),
    ]
