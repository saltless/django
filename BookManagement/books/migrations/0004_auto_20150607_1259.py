# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20150607_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publicationDate',
            field=models.DateField(null=True, blank=True),
        ),
    ]
