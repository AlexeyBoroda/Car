from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import path
from .models import Review, SeoSettings

# Register your models here.
admin.site.register(Review)

@admin.register(SeoSettings)
class SeoSettingsAdmin(admin.ModelAdmin):
    list_display = ("url", "title", "description", "keywords", "og_title")
    search_fields = ("url", "title", "description", "keywords", "og_title")
    actions = ['copy_seo_settings']

    def copy_seo_settings(self, request, queryset):
        if len(queryset) != 1:
            self.message_user(request, "Пожалуйста, выберите только одну запись для копирования.", messages.ERROR)
            return
        
        seo = queryset.first()
        new_url = f"{seo.url}-copy"
        
        try:
            new_seo = seo.copy(new_url)
            self.message_user(request, f"Настройки SEO успешно скопированы в новую запись с URL: {new_url}")
        except Exception as e:
            self.message_user(request, f"Ошибка при копировании: {str(e)}", messages.ERROR)
    
    copy_seo_settings.short_description = "Копировать выбранные настройки SEO"
