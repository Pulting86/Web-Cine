from rest_framework import serializers
from .models import *

class APISerializers(serializers.ModelSerializer):
    class Meta:
        model = API_Pelicula
        fields = '__all__'