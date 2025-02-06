from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('api/heatmap_data', views.get_latest_estimates, name='get_latest_estimates'),
]

urlpatterns += [
    path('auth/', include('django.contrib.auth.urls')),
]