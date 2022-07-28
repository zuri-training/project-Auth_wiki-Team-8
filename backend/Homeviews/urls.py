from django.urls import path
from .import views
app_name = 'homeviews'
urlpatterns = [
    path('', views.home_view, name="home"),
    path('about', views.about_view, name="about"),
    path('contact', views.contact_view, name="contact"),
    path('login', views.login_view, name="login"),
    path('register', views.register_view, name="register"),
]
