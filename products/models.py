from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    options = (
        ('Project Hours', 'Project Hours'),
        ('Marketing Templates', 'Marketing Templates'),
        ('Free consultation', 'Free consultation')
    )
    friendly_name = models.CharField(max_length=254, default="Project Hours", choices=options)
    name = models.CharField(max_length=254)    
    is_available_guest_user = models.BooleanField(null=True, blank=True)

    objects = models.Manager()    

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    priority = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )

    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.SET_NULL, default="")
    name = models.CharField(max_length=254)
    description_1 = models.CharField(max_length=100, blank=True)
    description_2 = models.CharField(max_length=100, blank=True)
    description_3 = models.CharField(max_length=100, blank=True)
    description_4 = models.CharField(max_length=100, blank=True)    
    price = models.DecimalField(max_digits=6, decimal_places=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    time_allocation_mins = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    is_digital = models.BooleanField(null=False)
    max_time_multiplier = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    pricing_priority = models.DecimalField(max_digits=6, decimal_places=0, null=True, default='4', choices=priority)

    objects = models.Manager()

    def __str__(self):
        return self.name
