# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0006_auto_20171119_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='seminarcounter',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
