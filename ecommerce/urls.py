from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

from carts.views import cart_home

from .views import (home_page, about_page, contact_page, login_page, register_page)

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', login_page, name='login'),
    url(r'^cart/', include('carts.urls')),
    url(r'^register/$', register_page, name='register'),
    url(r'^products/', include('products.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^tags/', include('tags.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
