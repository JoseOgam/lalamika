# Generated by Django 2.2.1 on 2019-06-12 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0013_auto_20190612_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transcript',
            name='unit',
        ),
    ]