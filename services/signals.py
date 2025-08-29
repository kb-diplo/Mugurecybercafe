from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Service, ServiceCategory

@receiver(pre_save, sender=Service)
def set_service_slug(sender, instance, *args, **kwargs):
    """
    Automatically generate a slug for the service if it doesn't exist or if the name has changed.
    """
    if not instance.slug or (instance.pk and 
                           sender.objects.get(pk=instance.pk).name != instance.name):
        instance.slug = slugify(instance.name)

# ServiceCategory doesn't have a slug field, so no signal needed
