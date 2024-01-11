from django.shortcuts import render
from rest_framework import viewsets
from .models import Medicine, Type
from .serializers import MedicineSerializer, TypeSerializer

# Create your views here.
class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
