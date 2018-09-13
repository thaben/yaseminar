# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20171119_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='receiver',
            field=models.ForeignKey(related_name='user_notification', to='userprofile.SimpleUser', null=True),
        ),
    ]
