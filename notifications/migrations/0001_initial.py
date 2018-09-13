# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20171117_2258'),
        ('seminar', '0006_auto_20171119_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('read', models.BooleanField(default=False)),
                ('n_sender', models.ForeignKey(blank=True, to='userprofile.AffiliateUser', null=True)),
                ('receiver', models.ForeignKey(related_name='users_notification_list', to='userprofile.SimpleUser', null=True)),
                ('s_name', models.ForeignKey(to='seminar.Seminar', null=True)),
            ],
        ),
    ]
