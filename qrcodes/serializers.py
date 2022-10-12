import os
from core.settings import BASE_DIR
from rest_framework.serializers import ModelSerializer
from qrcodes.models import QRCode

class QRCodeSerializer(ModelSerializer):
    class Meta:
        model = QRCode
        fields = '__all__'