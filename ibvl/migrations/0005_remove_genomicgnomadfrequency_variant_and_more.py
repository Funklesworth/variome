# Generated by Django 4.0 on 2024-05-29 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ibvl', '0004_rename_genomicibvlfrequency_genomicvariomefrequency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genomicgnomadfrequency',
            name='variant',
        ),
        migrations.RemoveField(
            model_name='genomicvariomefrequency',
            name='variant',
        ),
        migrations.RemoveField(
            model_name='snv',
            name='variant',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='gene',
        ),
        migrations.RemoveField(
            model_name='variantannotation',
            name='variant_transcript',
        ),
        migrations.RemoveField(
            model_name='variantconsequence',
            name='severity',
        ),
        migrations.RemoveField(
            model_name='variantconsequence',
            name='variant_transcript',
        ),
        migrations.RemoveField(
            model_name='varianttranscript',
            name='transcript',
        ),
        migrations.RemoveField(
            model_name='varianttranscript',
            name='variant',
        ),
        migrations.DeleteModel(
            name='Gene',
        ),
        migrations.DeleteModel(
            name='GenomicGnomadFrequency',
        ),
        migrations.DeleteModel(
            name='GenomicVariomeFrequency',
        ),
        migrations.DeleteModel(
            name='Severity',
        ),
        migrations.DeleteModel(
            name='SNV',
        ),
        migrations.DeleteModel(
            name='Transcript',
        ),
        migrations.DeleteModel(
            name='Variant',
        ),
        migrations.DeleteModel(
            name='VariantAnnotation',
        ),
        migrations.DeleteModel(
            name='VariantConsequence',
        ),
        migrations.DeleteModel(
            name='VariantTranscript',
        ),
    ]