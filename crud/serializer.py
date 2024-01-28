from rest_framework.serializers import ModelSerializer
from .models import INFOList

class INFOSerializer(ModelSerializer):
    class Meta:
        model= INFOList
        fields = '__all__'