# Generated by Django 2.2.1 on 2019-07-10 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0015_lecturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='contacts',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
