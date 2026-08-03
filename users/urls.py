from django.urls import path
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView 


urlpatterns = [
    path('register/',users_views.register,name = "register"),
    path('login/',auth_views.LoginView.as_view(template_name = "login.html"),name = "login"),
    path('logout/', users_views.user_logout, name='logout'),
]
