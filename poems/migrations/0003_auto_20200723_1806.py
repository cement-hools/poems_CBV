# Generated by Django 2.2.14 on 2020-07-23 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0002_poem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poem',
            options={'ordering': ('title',), 'verbose_name': 'Стихотворение'},
        ),
    ]
