# Generated by Django 2.2.1 on 2019-05-16 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0008_auto_20190514_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints',
            name='regno',
        ),
        migrations.AlterField(
            model_name='complaints',
            name='status',
            field=models.CharField(choices=[('In Queue', 'In Queue'), ('Complete', 'Complete')], max_length=30),
        ),
    ]