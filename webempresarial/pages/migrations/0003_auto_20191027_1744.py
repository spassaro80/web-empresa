# Generated by Django 2.2.5 on 2019-10-27 16:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20191026_1926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'ordering': ['order', 'title'], 'verbose_name': 'Página generica', 'verbose_name_plural': 'Páginas genéricas'},
        ),
        migrations.AlterField(
            model_name='pages',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Contexto'),
        ),
    ]