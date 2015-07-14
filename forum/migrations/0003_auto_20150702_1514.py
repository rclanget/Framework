# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20150702_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(null=True)),
                ('auteur', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='forum.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(null=True)),
                ('auteur', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('postmessage', models.ForeignKey(to='forum.PostMessage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Post_categorie',
            new_name='PostCategorie',
        ),
    ]
