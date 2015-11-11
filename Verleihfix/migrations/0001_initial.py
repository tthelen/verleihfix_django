# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lending',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('start', models.DateField()),
                ('duration', models.IntegerField()),
                ('status', models.CharField(max_length=1, choices=[('r', 'reserved'), ('l', 'lended')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('category', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('min_lending_span', models.IntegerField()),
                ('max_lending_span', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lending',
            name='thing',
            field=models.ForeignKey(to='Verleihfix.Thing'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lending',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
