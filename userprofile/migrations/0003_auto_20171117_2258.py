# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20171117_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simpleuser',
            old_name='users',
            new_name='user',
        ),
    ]
