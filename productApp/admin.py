from django.contrib import admin
from .models import brand_table, category_table, test_table, product_table, product_image
# Register your models here.

from django.utils.html import mark_safe


admin.site.register(brand_table)
admin.site.register(category_table)

admin.site.register(test_table)


class ProductImageInline(admin.TabularInline):
    model = product_image

    extra = 1  
    max_num = 10  
    fields = ['image', 'preview']  
    readonly_fields = ['preview']  
    
    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "No image"
    preview.short_description = 'Preview'
    


class ProductTableAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ['name', 'price', 'stock', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    # list_filter = ['is_active', 'choose_category', 'choose_brand']


admin.site.register(product_table, ProductTableAdmin)

admin.site.register(product_image)