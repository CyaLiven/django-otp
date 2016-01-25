# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from seahub.base.fields import LowerCaseCharField


class Migration(migrations.Migration):

    # dependencies = [
    #     migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    # ]

    operations = [
        migrations.CreateModel(
            name='StaticDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='The human-readable name of this device.', max_length=64)),
                ('confirmed', models.BooleanField(default=True, help_text='Is this device ready for use?')),
                # ('user', models.ForeignKey(help_text='The user that this device belongs to.', to=settings.AUTH_USER_MODEL)),
                ('user', LowerCaseCharField(max_length=255, help_text="The user that this device belongs to.")),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StaticToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=16, db_index=True)),
                ('device', models.ForeignKey(related_name='token_set', to='otp_static.StaticDevice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
