from django.urls import path, include, re_path
from contact import views as contact_views

app_name = 'contacts'
urlpatterns = [
    path('send/', contact_views.sendMail_view, name="sendContact"),
]
