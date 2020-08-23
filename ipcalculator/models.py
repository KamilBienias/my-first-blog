from django.db import models


class HostAndMask(models.Model):
    host_octet_1 = models.DecimalField(max_digits=3, decimal_places=0)
    host_octet_2 = models.DecimalField(max_digits=3, decimal_places=0)
    host_octet_3 = models.DecimalField(max_digits=3, decimal_places=0)
    host_octet_4 = models.DecimalField(max_digits=3, decimal_places=0)
    mask_octet_1 = models.DecimalField(max_digits=3, decimal_places=0)
    mask_octet_2 = models.DecimalField(max_digits=3, decimal_places=0)
    mask_octet_3 = models.DecimalField(max_digits=3, decimal_places=0)
    mask_octet_4 = models.DecimalField(max_digits=3, decimal_places=0)
