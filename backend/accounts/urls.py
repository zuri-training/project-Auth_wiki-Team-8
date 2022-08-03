from os import path
from django.urls import path
from django.contrib.auth.views import (PasswordResetDoneView, PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView)
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('signin/', views.signin_view, name="signin"),
    path('logout/', views.logout_view, name="logout"),
    # path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('password_change/', PasswordChangeView.as_view, name="password_change"),
    path('password_change/done/', PasswordChangeDoneView.as_view, name="password_change_done"),
    path('password_reset/', PasswordResetView.as_view, name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view, name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view, name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view, name="password_reset_complete"),
]
