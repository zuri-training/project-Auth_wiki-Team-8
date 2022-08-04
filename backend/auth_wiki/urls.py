from django.contrib import admin
from django.urls import path, include, re_path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('library/', include('librarys.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('about/', views.about),
    path('contact-us/', views.contact_us),
    path('', views.home),
    # path('', article_views.article_list, name="home"),
]
