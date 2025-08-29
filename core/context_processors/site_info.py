"""
Context processors for the core app.
"""
from django.conf import settings


def site_info(request):
    """
    Add site-wide context variables to all templates.
    """
    return {
        'SITE_NAME': getattr(settings, 'SITE_NAME', 'Mugure Cyber Services'),
        'SITE_URL': getattr(settings, 'SITE_URL', 'https://mugurecyber.co.ke'),
        'CONTACT_EMAIL': getattr(settings, 'CONTACT_EMAIL', 'mugurecyberservices@gmail.com'),
        'SUPPORT_EMAIL': getattr(settings, 'SUPPORT_EMAIL', 'mugurecyberservices@gmail.com'),
        'DEBUG': settings.DEBUG,
    }
