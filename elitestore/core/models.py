from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_value = models.CharField(max_length=7, blank=True, null=True)  # For web color representation
    
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # Additional details, if needed

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'color', 'size')  # Ensures each combination is unique

    def __str__(self):
        return f"{self.product.name} - {self.color.name} - {self.size.name}"
    
class Career(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()

    def __str__(self):
        return self.name
