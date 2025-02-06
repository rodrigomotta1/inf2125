from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from visualizer.views import SignUpView, CustomLoginView

urlpatterns = [
    path("", include("visualizer.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page=""), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)