# Generated by Django 2.2.5 on 2019-10-27 16:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191023_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default=datetime.datetime(2019, 10, 27, 16, 44, 14, 569617, tzinfo=utc), verbose_name='Publicado el '),
        ),
    ]
