from django.contrib import admin
from .models import Product, Category, Tag, Variation
from django.utils.html import format_html
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "parent_category")
    list_filter = ("name",)
    list_display_links = ('name',)
    # list_editable = ("",)
    search_fields = ("name",)
    preserve_filters = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","display_image", "description","category","active","list_tags")
    list_filter = ("name",)
    list_editable = ("active",)
    preserve_filters = True

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        else:
            return "No Image"
    def list_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    list_tags.short_description = 'Tags'

    display_image.allow_tags = True
    display_image.short_description = 'Image Preview'

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ("products", "size","stock","price", "sale", "color")
    list_filter = ("price",)
    list_editable = ("stock","price","sale","color", "size")
    preserve_filters = True


admin.site.register(Tag)