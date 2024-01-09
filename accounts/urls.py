from django.urls import path
from .views import SignUpView,register
from django.contrib.auth.views import LogoutView


urlpatterns = [
path("signup/", register, name="signup"),
# path("logout/",LogoutView.as_view(),name="logout"),
]