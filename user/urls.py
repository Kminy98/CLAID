from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user import views
from django.urls import path
app_name = 'user'

urlpatterns = [
    path("signup/", views.UserSignupView.as_view(), name="signup"),

    path("activate/<slug:uidb64>/<slug:token>/", views.UserActivate.as_view(), name="activate"),
    path("success/", views.active_success, name="success"),

    path("login/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", views.UserLogoutView.as_view(), name='logout'),
]