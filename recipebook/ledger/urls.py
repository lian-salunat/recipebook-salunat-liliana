from django.contrib.auth import views as auth_views
from django.urls import path

from .views import recipes_list, recipe

app_name = 'ledger'

urlpatterns = [
    path('recipes/', recipes_list, name='recipes_list'),
    path('recipe/<int:pk>/', recipe, name='recipe'),

    # Authentication
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            next_page='ledger:recipes_list',
        ),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='ledger:login'),
        name='logout',
    ),

    # Password reset flow
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            success_url='/password-reset/done/',
        ),
        name='password_reset',
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'password-reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
            success_url='/password-reset/complete/',
        ),
        name='password_reset_confirm',
    ),
    path(
        'password-reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
]