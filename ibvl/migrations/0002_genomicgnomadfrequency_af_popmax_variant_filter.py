# Generated by Django 4.2.1 on 2024-01-13 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibvl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genomicgnomadfrequency',
            name='af_popmax',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='variant',
            name='filter',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
