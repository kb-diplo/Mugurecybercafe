from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date', 'created_at')
    list_filter = ('status', 'published_date', 'created_at', 'author')
    search_fields = ('title', 'content', 'excerpt')
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('-published_date', '-created_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author')
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'featured_image')
        }),
        ('Publishing', {
            'fields': ('status', 'published_date')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)
