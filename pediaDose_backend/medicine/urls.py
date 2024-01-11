from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet, TypeViewSet

router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)
router.register(r'types', TypeViewSet)

app_name='medicine'

urlpatterns=[
    path('', include(router.urls)),

]