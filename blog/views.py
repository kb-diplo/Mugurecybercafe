from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BlogPost
from .forms import BlogPostForm


def blog_list(request):
    """Display list of published blog posts"""
    posts = BlogPost.objects.filter(status='published').order_by('-published_date')
    
    # Pagination
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'posts': page_obj,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """Display individual blog post"""
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    
    # Get related posts (same author or recent posts)
    related_posts = BlogPost.objects.filter(
        status='published'
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/blog_detail.html', context)


# Admin Blog Management Views
class BlogPostListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog/admin_blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return BlogPost.objects.all().order_by('-created_at')


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:admin_blog_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Blog post created successfully!')
        return super().form_valid(form)


class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:admin_blog_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Blog post updated successfully!')
        return super().form_valid(form)


class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:admin_blog_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Blog post deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
def blog_dashboard(request):
    """Blog management dashboard"""
    total_posts = BlogPost.objects.count()
    published_posts = BlogPost.objects.filter(status='published').count()
    draft_posts = BlogPost.objects.filter(status='draft').count()
    recent_posts = BlogPost.objects.order_by('-created_at')[:5]
    
    context = {
        'total_posts': total_posts,
        'published_posts': published_posts,
        'draft_posts': draft_posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/dashboard.html', context)
