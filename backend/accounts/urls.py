from os import path
from django.urls import path
from django.contrib.auth.views import (PasswordResetDoneView, PasswordResetView, PasswordResetCompleteView,
                                       PasswordResetConfirmView, PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView)
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.signin_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),
    path('password_change/', views.ChangePasswordView.as_view(),
         name="password_change"),
    path('password_change/done/', PasswordChangeDoneView.as_view(),
         name="password_change_done"),
    path('password_reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),

]
