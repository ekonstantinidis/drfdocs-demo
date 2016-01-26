# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.UUIDField(serialize=False, editable=False, primary_key=True, default=uuid.uuid4)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('is_owner', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.UUIDField(serialize=False, editable=False, primary_key=True, default=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('members', models.ManyToManyField(through='organisations.Membership', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Organisations',
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='organisation',
            field=models.ForeignKey(to='organisations.Organisation'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('organisation', 'user')]),
        ),
    ]
