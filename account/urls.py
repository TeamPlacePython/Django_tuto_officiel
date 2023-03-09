from re import template
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

from account import views

app_name = 'account'
urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change-password.html'
        ),
        name="change-password",
    ),
    path(
        'login/',
        LoginView.as_view(template_name='account/login.html'),
        name='login',
    ),
]
