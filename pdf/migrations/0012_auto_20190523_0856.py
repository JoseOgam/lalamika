# Generated by Django 2.2.1 on 2019-05-23 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0011_transcript_unit_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcript',
            name='unit_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
