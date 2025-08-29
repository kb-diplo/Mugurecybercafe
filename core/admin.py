from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'tagline', 'description')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email', 'address', 'whatsapp_number')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url'),
            'classes': ('collapse',)
        }),
        ('Homepage Content', {
            'fields': ('hero_title', 'hero_subtitle', 'about_title', 'about_content'),
            'classes': ('collapse',)
        }),
        ('Contact Page', {
            'fields': ('contact_title', 'contact_subtitle'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        try:
            return not SiteSettings.objects.exists()
        except:
            return True
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion
        return False
