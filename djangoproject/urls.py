from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', portfolio.views.home, name="home"),
    path('portfolio/', include('portfolio.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
