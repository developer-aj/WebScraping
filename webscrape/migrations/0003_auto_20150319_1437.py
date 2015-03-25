# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscrape', '0002_auto_20150319_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='site',
        ),
        migrations.DeleteModel(
            name='content',
        ),
        migrations.AddField(
            model_name='web',
            name='data',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='web',
            name='email',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
