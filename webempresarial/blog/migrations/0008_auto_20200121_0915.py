# Generated by Django 2.2.5 on 2020-01-21 08:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191101_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default=datetime.datetime(2020, 1, 21, 8, 15, 27, 443202, tzinfo=utc), verbose_name='Publicado el '),
        ),
    ]