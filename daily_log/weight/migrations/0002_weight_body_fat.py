# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weight',
            name='body_fat',
            field=models.FloatField(default=99),
            preserve_default=False,
        ),
    ]
