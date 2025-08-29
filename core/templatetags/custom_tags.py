"""
Custom template tags and filters for the core app.
"""
import re
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
@stringfilter
def phone_number(value):
    """Format a phone number for display."""
    if not value:
        return ''
    
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', str(value))
    
    # Format as Kenyan phone number: 254 7XX XXX XXX
    if len(digits) == 12 and digits.startswith('254'):
        return f"{digits[0:3]} {digits[3:6]} {digits[6:9]} {digits[9:12]}"
    # Format as local Kenyan number: 07XX XXX XXX
    if len(digits) == 10 and digits.startswith('0'):
        return f"{digits[0:4]} {digits[4:7]} {digits[7:10]}"
    # Format as international number with +: +254 7XX XXX XXX
    if len(digits) >= 9:
        return f"+{digits}"
    return value
    


@register.filter
def add_class(field, css_class):
    """Add a CSS class to a form field."""
    return field.as_widget(attrs={'class': css_class})


@register.filter
def is_list(value):
    """Check if a value is a list."""
    return isinstance(value, (list, tuple))


@register.simple_tag
def active_page(request, view_name, exact=False, **kwargs):
    """
    Return 'active' if the current page matches the given view name.
    
    Usage:
        {% active_page request 'view_name' %}
        {% active_page request 'app:view_name' %}
    """
    if not request or not hasattr(request, 'resolver_match'):
        return ''
    
    # Handle namespaced view names
    if ':' in view_name:
        app_name, view = view_name.split(':', 1)
        view_name = f'{app_name}:{view}'
    
    current_view = getattr(request.resolver_match, 'view_name', '')
    if not current_view:
        return ''
    
    # Check if the current view matches the given view name
    if exact:
        return 'active' if current_view == view_name else ''
    return 'active' if current_view.startswith(view_name) else ''


@register.filter
def get_item(dictionary, key):
    """Get a dictionary value by key."""
    if not isinstance(dictionary, dict):
        return ''
    return dictionary.get(key, '')


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Replace or add URL parameters while keeping existing ones.
    
    Usage:
        {% param_replace page=1 %}
    """
    if 'request' not in context:
        return ''
        
    params = context['request'].GET.copy()
    
    for key, value in kwargs.items():
        params[key] = value
    
    return params.urlencode()


@register.filter
def truncate_chars(value, max_length):
    """
    Truncate a string after a certain number of characters.
    
    Args:
        value: The string to truncate
        max_length: Maximum length before truncation
        
    Returns:
        str: Truncated string with ellipsis if needed
    """
    if not value:
        return ''
        
    str_value = str(value)
    if len(str_value) > int(max_length):
        return f"{str_value[:int(max_length)]}..."
    return str_value


@register.filter
def format_currency(value):
    """
    Format a number as Kenyan Shillings currency.
    
    Args:
        value: Numeric value to format
        
    Returns:
        str: Formatted currency string
    """
    if value in (None, ''):
        return 'KSh 0.00'
        
    try:
        return f"KSh {float(value):,.2f}"
    except (ValueError, TypeError):
        return str(value)


@register.filter
def get_range(value):
    """
    Return a range of numbers up to the given value.
    
    Args:
        value: The upper bound of the range
        
    Returns:
        range: Range from 1 to value (inclusive)
    """
    try:
        return range(1, int(value) + 1)
    except (ValueError, TypeError):
        return range(0)
