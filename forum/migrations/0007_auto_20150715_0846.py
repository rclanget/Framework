# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_remove_post_contenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sscategorie',
            field=models.ForeignKey(default=1, to='forum.PostSsCategorie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='categorie',
            field=models.ForeignKey(to='forum.PostCategorie'),
        ),
    ]
