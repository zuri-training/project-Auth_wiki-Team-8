from os import path
from django.urls import path, reverse_lazy
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
    path('password_reset/', PasswordResetView.as_view(template_name='accounts/reset_pass_form.html', email_template_name='accounts/reset_pass_email.html'), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='accounts/reset_pass_done.html'), name="password_reset/done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/reset_pass_confirm.html'),
         name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='accounts/change_pass_success.html'),
         name="password_reset_complete"),

]
