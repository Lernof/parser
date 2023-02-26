from rest_framework.routers import DefaultRouter
from resources import views


router = DefaultRouter()
router.register(r'resources', views.ResourcesViewSet, basename='resources')
router.register(r'items', views.ItemsViewSet, basename='items')

urlpatterns = router.urls