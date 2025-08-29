from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class ServiceCategory(models.Model):
    """Category for grouping services (e.g., Online Services, Cyber Services, etc.)"""
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Service Categories"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class Service(models.Model):
    """Services offered by Mugure Cyber Services"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    description = models.TextField(help_text="Detailed description of the service")
    short_description = models.CharField(max_length=255, help_text="Brief description for cards and lists")
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('services:service_detail', kwargs={'slug': self.slug})
