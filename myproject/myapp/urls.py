from rest_framework.routers import DefaultRouter
from .views import AdvViewSet

router =DefaultRouter()
router.register('api',AdvViewSet)


urlpatterns =  router.urls
