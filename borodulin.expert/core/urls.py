from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/coaching/', views.service_detail, {'service_slug': 'coaching'}, name='service_coaching'),
    path('services/training/', views.service_detail, {'service_slug': 'training'}, name='service_training'),
    path('services/masterclass/', views.service_detail, {'service_slug': 'masterclass'}, name='service_masterclass'),
    path('services/consulting/', views.service_detail, {'service_slug': 'consulting'}, name='service_consulting'),
    path('books/', views.books, name='books'),
    path('blog/', views.blog, name='blog'),
    path('videos/', views.videos, name='videos'),
    path('reviews/', views.reviews, name='reviews'),
    path('faq/', views.faq, name='faq'),
    path('checklists/', views.checklists, name='checklists'),
    path('tools/', views.tools, name='tools'),
    path('contacts/', views.contacts, name='contacts'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('privacy/', views.privacy, name='privacy'),
    path('consent/', views.consent, name='consent'),
] 