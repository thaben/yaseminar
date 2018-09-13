# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0002_notifications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='sender',
            new_name='n_sender',
        ),
    ]
