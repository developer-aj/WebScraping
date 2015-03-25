# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscrape', '0003_auto_20150319_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='web',
            old_name='data',
            new_name='emails',
        ),
        migrations.RemoveField(
            model_name='web',
            name='email',
        ),
        migrations.AddField(
            model_name='web',
            name='links',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
