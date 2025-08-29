from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Public blog URLs
    path('', views.blog_list, name='blog_list'),
    path('post/<slug:slug>/', views.blog_detail, name='post_detail'),
    
    # Admin blog management URLs
    path('admin/', views.BlogPostListView.as_view(), name='admin_blog_list'),
    path('admin/add/', views.BlogPostCreateView.as_view(), name='blog_create'),
    path('admin/<int:pk>/edit/', views.BlogPostUpdateView.as_view(), name='blog_edit'),
    path('admin/<int:pk>/delete/', views.BlogPostDeleteView.as_view(), name='blog_delete'),
    path('admin/dashboard/', views.blog_dashboard, name='blog_dashboard'),
]
