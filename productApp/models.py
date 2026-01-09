from django.db import models

# Create your models here.


# one class = one model = one table
# one field = one column

# ORM = Object Relational Mapping
# SQL = Structured Query Language

# brand_table.objects.all()
# brand_table.objects.filter(id = 1)
# brand_table.objects.create(title="hi", description="hello")

class brand_table(models.Model):
    title = models.CharField(max_length=199)
    description = models.TextField()

    def __str__(self):
        return self.title

    def count_product_specific_brands(self):
        filter_product = product_table.objects.filter(choose_brand=self)
        count_filter_product = filter_product.count()
        return count_filter_product


class category_table(models.Model):
    title = models.CharField(max_length=199)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def count_product_specific_category(self):
        filter_product = product_table.objects.filter(choose_category=self)
        count_filter_product = filter_product.count()
        return count_filter_product



class test_table(models.Model):
    name = models.CharField(max_length=199)
    description = models.TextField()
    price = models.IntegerField()
    weight = models.FloatField()
    active_status = models.BooleanField(default = False)
    email = models.EmailField()
    Entry_Date = models.DateField()
    Entry_Date_Time = models.DateTimeField()

    choose_brand = models.ForeignKey(brand_table, on_delete=models.CASCADE, related_name="choose_brand")
    choose_multiple_brand = models.ManyToManyField(brand_table, related_name='brand_table_info')
    choose_unique_brand = models.OneToOneField(brand_table, on_delete=models.CASCADE, related_name="choose_unique_brand")


class product_table(models.Model):
    name = models.CharField(max_length=199)
    slug = models.SlugField(max_length=199, unique=True, blank=True)
    description = models.TextField(null=True, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    choose_brand = models.ForeignKey(brand_table, on_delete=models.CASCADE)
    choose_category = models.ForeignKey(category_table, on_delete=models.CASCADE)

    image = models.ImageField(upload_to = 'product_img/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    
    def filter_assigned_images(self):
        filter_product_images = product_image.objects.filter(product_info = self)
        return filter_product_images


class product_image(models.Model):
    product_info = models.ForeignKey(product_table, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'product_img/', blank=True, null=True)