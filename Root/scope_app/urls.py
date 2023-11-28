from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from scope_app.views import DinoViewSets


router = DefaultRouter()
router.register("dinos", DinoViewSets, basename="dino")
# router.register("zones", ZoneLocationViewSet, basename="zone")

# urlpatterns = [
#     #coming
#     path('', include(router.urls)),
    
# ]

urlpatterns = router.urls