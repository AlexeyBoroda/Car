from django.db import models

# Create your models here.

class Review(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст отзыва')
    image = models.ImageField(upload_to='review/', verbose_name='Фото', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')

    def __str__(self):
        return f'{self.author}: {self.text[:30]}...'

class SeoSettings(models.Model):
    url = models.CharField(max_length=255, unique=True, verbose_name="URL или имя страницы")
    title = models.CharField(max_length=255, verbose_name="Title", blank=True)
    description = models.TextField(verbose_name="Description", blank=True)
    keywords = models.CharField(max_length=255, verbose_name="Keywords", blank=True)
    canonical = models.URLField(verbose_name="Canonical URL", blank=True)
    robots = models.CharField(max_length=50, verbose_name="Robots", blank=True, default="index, follow")
    author = models.CharField(max_length=100, verbose_name="Author", blank=True)
    og_title = models.CharField(max_length=255, verbose_name="OG Title", blank=True)
    og_description = models.TextField(verbose_name="OG Description", blank=True)
    og_type = models.CharField(max_length=50, verbose_name="OG Type", blank=True, default="website")
    og_site_name = models.CharField(max_length=100, verbose_name="OG Site Name", blank=True)
    og_locale = models.CharField(max_length=20, verbose_name="OG Locale", blank=True, default="ru_RU")
    og_url = models.URLField(verbose_name="OG URL", blank=True)
    og_image = models.ImageField(upload_to='seo/', verbose_name="OG Image", blank=True, null=True)
    og_image_width = models.PositiveIntegerField(verbose_name="OG Image Width", blank=True, null=True)
    og_image_height = models.PositiveIntegerField(verbose_name="OG Image Height", blank=True, null=True)
    twitter_card = models.CharField(max_length=50, verbose_name="Twitter Card", blank=True, default="summary_large_image")
    twitter_site = models.CharField(max_length=100, verbose_name="Twitter Site", blank=True)
    twitter_creator = models.CharField(max_length=100, verbose_name="Twitter Creator", blank=True)
    schema_jsonld = models.TextField(verbose_name="Schema.org JSON-LD", blank=True)
    custom_meta = models.TextField(verbose_name="Дополнительные мета-теги (raw HTML)", blank=True)

    def __str__(self):
        return self.url

    def copy(self, new_url):
        """
        Создает копию текущего объекта SeoSettings с новым URL
        """
        # Создаем новый объект с теми же значениями полей
        new_seo = SeoSettings(
            url=new_url,
            title=self.title,
            description=self.description,
            keywords=self.keywords,
            canonical=self.canonical,
            robots=self.robots,
            author=self.author,
            og_title=self.og_title,
            og_description=self.og_description,
            og_type=self.og_type,
            og_site_name=self.og_site_name,
            og_locale=self.og_locale,
            og_url=self.og_url,
            og_image=self.og_image,
            og_image_width=self.og_image_width,
            og_image_height=self.og_image_height,
            twitter_card=self.twitter_card,
            twitter_site=self.twitter_site,
            twitter_creator=self.twitter_creator,
            schema_jsonld=self.schema_jsonld,
            custom_meta=self.custom_meta
        )
        new_seo.save()
        return new_seo
