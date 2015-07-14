# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20150708_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='closeby',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
