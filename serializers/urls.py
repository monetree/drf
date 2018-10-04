
from django.contrib import admin
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import *
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('companies',CompanyView)
router.register('languages',LanguageView)
router.register('frameworks',FrameworksView)
router.register('technologies',TechnologiesView)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
