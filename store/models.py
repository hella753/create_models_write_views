from django.db import models


class Category(models.Model):
    category_name = models.CharField("სახელი", max_length=100)
    category_description = models.TextField("აღწერა", null=True, blank=True)
    parent_category = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="ზეკატეგორია"
    )
    category_level = models.IntegerField("დონე", null=True, blank=True)

    def __str__(self):
        return f"{self.category_name}"


class Product(models.Model):
    product_name = models.CharField("სახელი", max_length=100)
    product_price = models.DecimalField(
        "ფასი",
        max_digits=10,
        decimal_places=2
    )
    product_description = models.TextField("აღწერა", null=True, blank=True)
    product_image = models.ImageField(
        "სურათი",
        help_text="ატვირთეთ ფოტოსურათი",
        blank=True,
        null=True
    )
    product_category = models.ManyToManyField(
        "Category",
        verbose_name="კატეგორია"
    )

    def __str__(self):
        return f"{self.id} | {self.product_name}"
