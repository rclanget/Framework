# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20150703_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='contenu',
        ),
    ]
