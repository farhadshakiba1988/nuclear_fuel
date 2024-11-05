from django.db import models


class Recepit(models.Model):
    MBA_CHOICES = [
        ('IR1B', 'IR1B'),
        ('IR2B', 'IR2B'),
        ('IR3B', 'IR3B'),

    ]

    IC_CODE_CHOICES = [
        ('DI', 'DI'),
        ('FW', 'FW'),
        ('GA', 'GA'),
        # Add other choices here
    ]

    MDC_CHOICES = [
        ('BQ1F', 'BQ1F'),
        ('BQ1G', 'BQ1G'),
        # Add other choices here
    ]

    OBL_CODE_CHOICES = [
        ('P', 'P'),
    ]

    ELT_CODE_CHOICES = [
        ('D', 'D'),
        ('E', 'E'),
        ('N', 'N'),
        ('P', 'P'),
        ('T', 'T'),
    ]
    FUEL_TYPE_CHOICES = [
        ('16', '16'),
        ('24', '24'),
        ('24B20', '24B20'),
        ('24B36', '24B36'),
        ('36', '36'),
        ('36B20', '36B20'),
        ('36B36', '36B36'),
        ('40', '40'),
        ('40B20', '40B20'),
        ('40B36', '40B36'),
        ('40B50', '40B50'),
    ]

    MBA = models.CharField(max_length=20, choices=MBA_CHOICES, blank=True)
    item_id = models.CharField(max_length=100, blank=True)
    container_id = models.CharField(max_length=100, blank=True)
    ic_date = models.DateField(null=True, blank=True)
    ic_code = models.CharField(max_length=20, choices=IC_CODE_CHOICES, blank=True)
    from_mba = models.CharField(max_length=20, choices=MBA_CHOICES, blank=True)
    mdc = models.CharField(max_length=20, choices=MDC_CHOICES, blank=True)
    obl_code = models.CharField(max_length=20, choices=OBL_CODE_CHOICES, blank=True)
    to_mba = models.CharField(max_length=20, choices=MBA_CHOICES, blank=True)
    no_of_items = models.PositiveIntegerField(default=1)
    elt_code = models.CharField(max_length=2, choices=ELT_CODE_CHOICES, blank=True)
    uo2_wf = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    elt_wf = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    enr = models.DecimalField(max_digits=5, decimal_places=2, default=1.60)
    iso_code = models.CharField(max_length=2, blank=True)
    iso_wf = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    burnup = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    mb = models.CharField(max_length=2, blank=True)
    fuel_type = models.CharField(max_length=6, choices=FUEL_TYPE_CHOICES, verbose_name="Fuel Type", blank=True,
                                 null=True)

    notes = models.CharField(max_length=255, verbose_name="Notes", blank=True, null=True)
    mat_descr = models.CharField(max_length=255, verbose_name="Mat Descr", blank=True, null=True)
    total_weight_kg = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total WT (KG)", blank=True,
                                          null=True)

    date_of_production = models.DateField(verbose_name="Date Of Production")
    cps_ar_bar = models.CharField(max_length=100, verbose_name="CPS AR/BAR", blank=True, null=True)
    drawing_no = models.CharField(max_length=100, verbose_name="Drawing NO", blank=True, null=True)

    product_images = models.FileField(upload_to='product_images/', blank=True)

    class Meta:
        verbose_name = "Inset Receipt"
        verbose_name_plural = "Inset Receipts"

    def __str__(self):
        return f"Receipt for {self.item_id}"
