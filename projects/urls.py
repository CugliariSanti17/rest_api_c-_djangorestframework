from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'project')
# Primer parametro: Nombre de la ruta (path)
# Segundo parametro: Configuracion de la base de datos
# Tercer parametro: Nombre de la ruta

urlpatterns = router.urls
