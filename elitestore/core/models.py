from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ('product', 'color', 'size')  # Ensures each combination is unique

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.size}"
