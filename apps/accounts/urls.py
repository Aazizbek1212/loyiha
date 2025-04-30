from django.urls import path

from apps.accounts.views import login_user, profile_update,  register_user, logout_user


urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logaout/', logout_user, name='logout'),
    path('profile/', profile_update, name='profile'),  # ProfileView ni import qilishni unutmang
]