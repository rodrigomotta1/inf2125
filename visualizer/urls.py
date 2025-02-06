from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_information/', views.upload_information, name='upload_information'),
    path('api/update_settings/', views.update_user_settings, name='update_user_settings'),
    path("api/place_details/<int:place_id>/", views.get_place_details, name="get_place_details"),
    path("api/toggle_saved_place/", views.toggle_saved_place, name="toggle_saved_place"),
]

urlpatterns += [
    path('auth/', include('django.contrib.auth.urls')),
]