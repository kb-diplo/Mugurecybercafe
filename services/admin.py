from django.contrib import admin
from .models import ServiceCategory, Service

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    list_editable = ('is_active', 'order')
    ordering = ('order', 'name')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_featured', 'is_active', 'order', 'created_at')
    list_filter = ('category', 'is_featured', 'is_active', 'created_at')
    search_fields = ('name', 'description', 'short_description')
    list_editable = ('is_featured', 'is_active', 'order')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order', 'name')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category')
        }),
        ('Content', {
            'fields': ('short_description', 'description', 'icon')
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )
