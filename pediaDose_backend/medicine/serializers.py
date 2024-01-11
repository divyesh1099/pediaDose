from rest_framework import serializers
from .models import Medicine, Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name', 'formula_min', 'formula_max', 'information']

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'types', 'information', 'formula_min', 'formula_max']
