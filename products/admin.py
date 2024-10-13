from django.contrib import admin

from .models import Product, File, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enabled', 'created_at']
    list_filter = ['is_enabled', 'parent']
    search_fields = ['title']

class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['file', 'title', 'is_enabled', 'file_type']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enabled', 'created_at']
    list_filter = ['is_enabled']
    filter_horizontal = ['categories']
    search_fields = ['title']
    inlines = [FileInlineAdmin]



