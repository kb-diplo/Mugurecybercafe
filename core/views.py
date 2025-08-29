from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.defaults import page_not_found, server_error as server_error_view

# Home page view
def home(request):
    """Render the home page"""
    context = {
        'title': 'Home',
    }
    return render(request, 'core/home.html', context)

# About page view
def about(request):
    """Render the about page"""
    context = {
        'title': 'About Us',
    }
    return render(request, 'core/about.html', context)

# Contact page view
def contact(request):
    """Handle contact form submission"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Basic validation
        if not all([name, email, subject, message]):
            messages.error(request, 'Please fill in all required fields.')
        else:
            # Send email
            email_subject = f'New Contact Form: {subject}'
            email_message = f'''
            Name: {name}
            Email: {email}
            
            Message:
            {message}
            '''
            
            try:
                send_mail(
                    subject=email_subject,
                    message=email_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your message. We will get back to you soon!')
                return redirect('contact')
            except BadHeaderError:
                messages.error(request, 'Invalid header found in the form submission.')
            except Exception as e:
                messages.error(request, f'There was an error sending your message. Please try again later. Error: {str(e)}')
    
    context = {
        'title': 'Contact Us',
        'form_data': {
            'name': request.POST.get('name', ''),
            'email': request.POST.get('email', ''),
            'subject': request.POST.get('subject', ''),
            'message': request.POST.get('message', ''),
        }
    }
    return render(request, 'core/contact.html', context)


def handler404(request, exception, template_name='core/404.html'):
    """Custom 404 error handler"""
    context = {
        'title': 'Page Not Found',
        'exception': str(exception) if settings.DEBUG else None
    }
    return page_not_found(request, exception, template_name, context)


def handler500(request, template_name='core/500.html'):
    """Custom 500 error handler"""
    context = {
        'title': 'Server Error',
    }
    return server_error_view(request, template_name=template_name, context=context)
