from django.db import models
from .variant import Variant


class GenomicIBVLFrequency(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, db_column='variant')
    af_tot = models.DecimalField(decimal_places=10, max_digits=12)
    af_xy = models.DecimalField(decimal_places=10, max_digits=12, null=True)
    af_xx = models.DecimalField(decimal_places=10, max_digits=12, null=True)
    ac_tot = models.DecimalField(decimal_places=3, max_digits=12)
    ac_xy = models.DecimalField(decimal_places=3, max_digits=12, null=True)
    ac_xx = models.DecimalField(decimal_places=3, max_digits=12, null=True)
    an_tot = models.DecimalField(decimal_places=3, max_digits=12, null=True)
    an_xy = models.DecimalField(decimal_places=3, max_digits=12, null=True)
    an_xx = models.DecimalField(decimal_places=3, max_digits=12, null=True)
    hom_tot = models.DecimalField(decimal_places=3, max_digits=12)
    hom_xy = models.DecimalField(decimal_places=3, max_digits=12)
    hom_xx = models.DecimalField(decimal_places=3, max_digits=12)
    quality = models.DecimalField(decimal_places=3, max_digits=12)

    class Meta:
        db_table = "genomic_ibvl_frequencies"
        verbose_name_plural = 'Genomic IBVL Frequencies'

    def __str__(self):
        return self.variant.variant_id