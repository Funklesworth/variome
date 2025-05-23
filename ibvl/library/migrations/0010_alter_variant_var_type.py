# Generated by Django 4.2.13 on 2024-11-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0009_alter_genomicvariomefrequency_ac_tot_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variant",
            name="var_type",
            field=models.CharField(
                choices=[
                    ("SNP", "SNP"),
                    ("M", "Mitochondrial"),
                    ("SV", "SV"),
                    ("INDEL", "INDEL"),
                ],
                max_length=30,
            ),
        ),
    ]
