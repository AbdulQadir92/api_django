from django.contrib import admin
from django.urls import path, include

## saving images to database
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'))
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
