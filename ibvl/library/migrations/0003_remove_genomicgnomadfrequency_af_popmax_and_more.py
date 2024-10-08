# Generated by Django 4.2.13 on 2024-09-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_alter_snv_length"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="genomicgnomadfrequency",
            name="af_popmax",
        ),
        migrations.AlterField(
            model_name="genomicgnomadfrequency",
            name="ac_tot",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="genomicgnomadfrequency",
            name="an_tot",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="genomicgnomadfrequency",
            name="hom_tot",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="genomicvariomefrequency",
            name="ac_tot",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="genomicvariomefrequency",
            name="an_tot",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="genomicvariomefrequency",
            name="hom_tot",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="genomicvariomefrequency",
            name="hom_xx",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="genomicvariomefrequency",
            name="hom_xy",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="genomicvariomefrequency",
            name="quality",
            field=models.IntegerField(),
        ),
    ]
