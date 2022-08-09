from django.contrib import admin
from django.urls import path, include, re_path
from .import views
from librarys import views as library_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('library/', include('librarys.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('about/', views.about),
    path('faq/', views.faq),
    path('contact-us/', views.contact_us),
    path('', views.home, name='home'),
    # path('', article_views.article_list, name="home"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve,
                        {'document_root': settings.MEDIA_ROOT, }), ]
