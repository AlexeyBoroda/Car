from django.shortcuts import render
from .models import Review, SeoSettings
import random
from types import SimpleNamespace
from .seo_defaults import SEO_DEFAULTS

# Create your views here.

def index(request):
    reviews = Review.objects.order_by('-created_at')[:3]
    seo = SeoSettings.objects.filter(url='/').first()
    if not seo:
        seo = SimpleNamespace(**SEO_DEFAULTS)
    return render(request, 'core/index.html', {'reviews': reviews, 'seo': seo})

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def books(request):
    return render(request, 'core/books.html')

def blog(request):
    return render(request, 'core/blog.html')

def videos(request):
    return render(request, 'core/videos.html')

def reviews(request):
    reviews = Review.objects.order_by('-created_at')
    return render(request, 'core/reviews.html', {'reviews': reviews})

def faq(request):
    return render(request, 'core/faq.html')

def checklists(request):
    return render(request, 'core/checklists.html')

def tools(request):
    return render(request, 'core/tools.html')

def contacts(request):
    return render(request, 'core/contacts.html')

def cabinet(request):
    return render(request, 'core/cabinet.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def consent(request):
    return render(request, 'core/consent.html')
