from django.db import models
from rest_framework import fields, serializers
from core.models import Arte

class ArteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arte
        fields = ['numarticulo','nombre','precio','autor','categoria']