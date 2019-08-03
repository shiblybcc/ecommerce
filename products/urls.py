from django.conf.urls import url

from .views import (ProductListView, ProductFeaturedDetailSlugView)

app_name = 'products'

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductFeaturedDetailSlugView.as_view(), name='detail'),
]
