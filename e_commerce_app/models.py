from django.db import models

class Products(models.Model):
    product_id = models.PositiveBigIntegerField(primary_key=True)
    product_title = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_desc = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    available_qty = models.IntegerField(default=0)
<<<<<<< HEAD
    product_img = models.ImageField(upload_to='products/', blank=True, null=True)
=======
    product_img_url = models.CharField(max_length=300, blank=True)
>>>>>>> 25350bf (lab task 3)

    def __str__(self):
        return self.product_title