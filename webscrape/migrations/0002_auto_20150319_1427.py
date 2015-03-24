# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscrape', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.TextField()),
                ('data', models.TextField()),
                ('site', models.ForeignKey(to='webscrape.web')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='web',
            name='data',
        ),
        migrations.RemoveField(
            model_name='web',
            name='email',
        ),
    ]
