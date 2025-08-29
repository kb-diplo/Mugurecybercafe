from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from .models import Service, ServiceCategory
from .forms import ServiceForm, ServiceCategoryForm

class ServiceListView(ListView):
    model = Service
    template_name = 'services/public_service_list.html'
    context_object_name = 'services'
    
    def get_queryset(self):
        return Service.objects.filter(is_active=True).select_related('category').order_by('category__order', 'order', 'name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ServiceCategory.objects.filter(is_active=True).prefetch_related('services').order_by('order', 'name')
        return context

class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services:service_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Service created successfully!')
        return super().form_valid(form)

class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services:service_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Service updated successfully!')
        return super().form_valid(form)

class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('services:service_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Service deleted successfully!')
        return super().delete(request, *args, **kwargs)

# Service Category Views
class ServiceCategoryListView(LoginRequiredMixin, ListView):
    model = ServiceCategory
    template_name = 'services/category_list.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return ServiceCategory.objects.annotate(service_count=Count('services')).order_by('order', 'name')

class ServiceCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ServiceCategory
    form_class = ServiceCategoryForm
    template_name = 'services/category_form.html'
    success_url = reverse_lazy('services:category_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Category created successfully!')
        return super().form_valid(form)

class ServiceCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceCategory
    form_class = ServiceCategoryForm
    template_name = 'services/category_form.html'
    success_url = reverse_lazy('services:category_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Category updated successfully!')
        return super().form_valid(form)

class ServiceCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceCategory
    template_name = 'services/category_confirm_delete.html'
    success_url = reverse_lazy('services:category_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Category deleted successfully!')
        return super().delete(request, *args, **kwargs)

@login_required
def service_dashboard(request):
    categories = ServiceCategory.objects.annotate(service_count=Count('services'))
    services = Service.objects.select_related('category').order_by('category__order', 'order')
    
    context = {
        'categories': categories,
        'services': services,
    }
    return render(request, 'services/dashboard.html', context)
