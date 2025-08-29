from django.db import models

class SiteSettings(models.Model):
    """Website settings that can be edited through admin"""
    site_name = models.CharField(max_length=100, default="Mugure Cyber Services")
    tagline = models.CharField(max_length=200, default="Your Trusted Cyber Cafe in Gatundu North")
    description = models.TextField(default="Providing reliable internet, printing, and online services to the Kamwangi community since 2020.")
    phone = models.CharField(max_length=20, default="+254 712 345 678")
    email = models.EmailField(default="info@mugurecyber.com")
    address = models.TextField(default="Kamwangi Market, Gatundu North")
    whatsapp_number = models.CharField(max_length=20, default="254712345678")
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    
    # Hero section content
    hero_title = models.CharField(max_length=200, default="Your Trusted Cyber Cafe in Gatundu North")
    hero_subtitle = models.TextField(default="Providing reliable internet, printing, and online services to the Kamwangi community since 2020.")
    
    # About section
    about_title = models.CharField(max_length=200, default="About Mugure Cyber Services")
    about_content = models.TextField(default="We have been serving the Kamwangi community with reliable cyber services since 2020.")
    
    # Contact section
    contact_title = models.CharField(max_length=200, default="Get in Touch")
    contact_subtitle = models.TextField(default="Ready to help with all your digital needs")
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return self.site_name
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def get_settings(cls):
        """Get or create site settings"""
        settings, created = cls.objects.get_or_create(pk=1)
        return settings
