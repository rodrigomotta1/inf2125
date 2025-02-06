from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/update_settings/', views.update_user_settings, name='update_user_settings'),
]

urlpatterns += [
    path('auth/', include('django.contrib.auth.urls')),
]