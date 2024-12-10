from rest_framework.routers import DefaultRouter
from core.views import LocalViewSet, UsuarioViewSet, AvisoViewSet, InformacaoViewSet, PrevisaoViewSet

router = DefaultRouter()
router.register(r'locais', LocalViewSet, basename='locais')
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'avisos', AvisoViewSet, basename='avisos')
router.register(r'informacoes', InformacaoViewSet, basename='informacoes')
router.register(r'previsoes', PrevisaoViewSet, basename='previsoes')

urlpatterns = router.urls