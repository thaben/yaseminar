# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0004_auto_20171119_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='s_name',
            field=models.ForeignKey(to='seminar.Seminar', null=True),
        ),
    ]
