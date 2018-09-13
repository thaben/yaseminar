# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0003_auto_20171119_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='s_name',
            field=models.ForeignKey(default=1, to='seminar.Seminar'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notifications',
            name='n_sender',
            field=models.ForeignKey(blank=True, to='userprofile.AffiliateUser', null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='receiver',
            field=models.ForeignKey(related_name='users_notification_list', to='userprofile.SimpleUser', null=True),
        ),
    ]
