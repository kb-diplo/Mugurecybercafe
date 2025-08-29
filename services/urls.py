from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    # Service URLs
    path('', views.ServiceListView.as_view(), name='service_list'),
    path('add/', views.ServiceCreateView.as_view(), name='service_create'),
    path('<int:pk>/edit/', views.ServiceUpdateView.as_view(), name='service_edit'),
    path('<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),
    
    # Category URLs
    path('categories/', views.ServiceCategoryListView.as_view(), name='category_list'),
    path('categories/add/', views.ServiceCategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', views.ServiceCategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.ServiceCategoryDeleteView.as_view(), name='category_delete'),
    
    # Dashboard
    path('dashboard/', views.service_dashboard, name='dashboard'),
]
