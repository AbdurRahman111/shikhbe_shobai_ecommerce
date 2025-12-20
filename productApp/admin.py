from django.contrib import admin
from .models import brand_table, category_table, test_table, product_table
# Register your models here.


admin.site.register(brand_table)
admin.site.register(category_table)

admin.site.register(test_table)

admin.site.register(product_table)