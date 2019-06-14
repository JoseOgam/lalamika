# Generated by Django 2.2.1 on 2019-06-12 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0012_auto_20190523_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transcript',
            name='marks',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='unit_title',
        ),
        migrations.AddField(
            model_name='complaints',
            name='transcript',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pdf.Transcript'),
        ),
        migrations.AddField(
            model_name='unit',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.DecimalField(decimal_places=1, max_digits=13)),
                ('transcript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf.Transcript')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf.Unit')),
            ],
        ),
    ]
