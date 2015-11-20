from django.conf.urls import patterns, url
from django.contrib import admin
from .views import Index

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'TFG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Inicio

    url(r'^$', Index.as_view(), name='index'),
]
