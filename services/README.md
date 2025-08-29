# Service Management System

This module provides a comprehensive service management system for Mugure Cyber Services, allowing administrators to manage services and their categories through a user-friendly interface.

## Features

### Service Management
- Create, read, update, and delete services
- Categorize services with icons and descriptions
- Mark services as featured or active/inactive
- Reorder services using the order field
- Search and filter services

### Category Management
- Create and manage service categories
- Set display order for categories
- Toggle category visibility
- View services within each category

### User Interface
- Responsive design using Bootstrap 5
- Intuitive dashboard with statistics
- Live preview of service and category changes
- Confirmation dialogs for destructive actions
- Form validation and error handling

## Models

### Service
- `name`: Name of the service
- `slug`: URL-friendly version of the name
- `category`: ForeignKey to ServiceCategory
- `description`: Detailed description of the service
- `short_description`: Brief summary for listings
- `icon`: Font Awesome icon class
- `is_featured`: Boolean to feature the service
- `is_active`: Boolean to enable/disable the service
- `order`: Integer for manual sorting
- `created_at`: Timestamp of creation
- `updated_at`: Timestamp of last update

### ServiceCategory
- `name`: Name of the category
- `slug`: URL-friendly version of the name
- `description`: Description of the category
- `icon`: Font Awesome icon class
- `is_active`: Boolean to enable/disable the category
- `order`: Integer for manual sorting
- `created_at`: Timestamp of creation
- `updated_at`: Timestamp of last update

## Views

### Service Views
- `ServiceListView`: List all services with filtering and pagination
- `ServiceCreateView`: Form to create a new service
- `ServiceUpdateView`: Form to edit an existing service
- `ServiceDeleteView`: Confirmation and deletion of a service
- `service_dashboard`: Overview dashboard with statistics

### Category Views
- `ServiceCategoryListView`: List all categories
- `ServiceCategoryCreateView`: Form to create a new category
- `ServiceCategoryUpdateView`: Form to edit an existing category
- `ServiceCategoryDeleteView`: Confirmation and deletion of a category

## Templates

### Service Templates
- `service_list.html`: Displays all services in a table
- `service_form.html`: Form for adding/editing services
- `service_confirm_delete.html`: Confirmation for service deletion
- `dashboard.html`: Service management dashboard

### Category Templates
- `category_list.html`: Displays all categories
- `category_form.html`: Form for adding/editing categories
- `category_confirm_delete.html`: Confirmation for category deletion

## URLs

```python
# Service URLs
path('', ServiceListView.as_view(), name='service_list'),
path('add/', ServiceCreateView.as_view(), name='service_create'),
path('<int:pk>/edit/', ServiceUpdateView.as_view(), name='service_edit'),
path('<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),

# Category URLs
path('categories/', ServiceCategoryListView.as_view(), name='category_list'),
path('categories/add/', ServiceCategoryCreateView.as_view(), name='category_create'),
path('categories/<int:pk>/edit/', ServiceCategoryUpdateView.as_view(), name='category_edit'),
path('categories/<int:pk>/delete/', ServiceCategoryDeleteView.as_view(), name='category_delete'),

# Dashboard
path('dashboard/', service_dashboard, name='dashboard'),
```

## Installation

1. Add 'services' to your `INSTALLED_APPS` in `settings.py`:
   ```python
   INSTALLED_APPS = [
       # ...
       'services',
   ]
   ```

2. Include the service URLs in your project's `urls.py`:
   ```python
   path('services/', include('services.urls', namespace='services')),
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Usage

1. Access the service management dashboard at `/services/dashboard/`
2. Create categories to organize your services
3. Add services to each category
4. Use the admin interface at `/admin/services/` for advanced management

## Dependencies

- Django 4.2+
- Django Crispy Forms
- Bootstrap 5
- Font Awesome 6
- Python 3.8+

## Customization

### Styling
Customize the appearance by overriding the following CSS classes in your project's static files:
- `.service-card`: Service card styling
- `.category-badge`: Category badge styling
- `.action-buttons`: Action button groups

### Icons
Icons are provided by Font Awesome. You can change icons by modifying the `icon` field in the admin or forms.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
