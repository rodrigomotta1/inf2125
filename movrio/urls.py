from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from visualizer.views import SignUpView

urlpatterns = [
    path('', include("visualizer.urls")),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page=""), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]