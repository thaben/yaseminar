# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0005_auto_20171119_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='n_sender',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='s_name',
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
    ]
