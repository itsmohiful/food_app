from django.urls import path
from django.contrib.auth import views as auth_view
from . import views as accounts_view


urlpatterns = [
    path('register/',accounts_view.register,name='register'),
    path('login/',auth_view.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/',accounts_view.user_profile,name='user-profile'),
]
