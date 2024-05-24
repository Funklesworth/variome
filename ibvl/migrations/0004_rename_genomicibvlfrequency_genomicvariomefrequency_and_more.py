# Generated by Django 4.2.1 on 2024-05-16 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ibvl', '0001_squashed_0003_alter_genomicgnomadfrequency_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GenomicIBVLFrequency',
            new_name='GenomicVariomeFrequency',
        ),
        migrations.AlterModelOptions(
            name='genomicvariomefrequency',
            options={'verbose_name_plural': 'Genomic Variome Frequencies'},
        ),
        migrations.AlterField(
            model_name='snv',
            name='variant',
            field=models.ForeignKey(db_column='variant', on_delete=django.db.models.deletion.CASCADE, related_name='snv', to='ibvl.variant'),
        ),
        migrations.AlterField(
            model_name='variantannotation',
            name='hgvsp',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='variantannotation',
            name='polyphen',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='variantannotation',
            name='sift',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='variantannotation',
            name='variant_transcript',
            field=models.ForeignKey(db_column='variant_transcript', on_delete=django.db.models.deletion.CASCADE, related_name='annotation', to='ibvl.varianttranscript'),
        ),
        migrations.AlterField(
            model_name='variantconsequence',
            name='variant_transcript',
            field=models.ForeignKey(db_column='variant_transcript', on_delete=django.db.models.deletion.CASCADE, related_name='consequence', to='ibvl.varianttranscript'),
        ),
        migrations.AlterField(
            model_name='varianttranscript',
            name='hgvsc',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterModelTable(
            name='genomicvariomefrequency',
            table='genomic_variome_frequencies',
        ),
    ]