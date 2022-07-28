from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from Homeviews import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('Libraryapp.urls')),
    path('', home_views.home_view, name="home"),
    path('home/', include('Homeviews.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve,
                        {'document_root': settings.MEDIA_ROOT, }), ]
