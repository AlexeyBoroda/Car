from .models import SeoSettings
from .seo_defaults import SEO_DEFAULTS

def seo_defaults(request):
    path = request.path
    seo = SeoSettings.objects.filter(url=path).first() or SeoSettings.objects.filter(url='default').first()
    return {"SEO": seo, "SEO_DEFAULTS": SEO_DEFAULTS} 