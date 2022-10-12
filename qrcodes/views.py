import os
import qrcode
import random
from pathlib import Path
from django.core.files import File
from core.settings import BASE_DIR
from rest_framework.views import APIView
from rest_framework.response import Response
from qrcodes.models import QRCode
from qrcodes.serializers import QRCodeSerializer

class GenerateCodeView(APIView):
    def post(self, request):
        try:
            name = request.data['name']
            description = request.data['description']
            url = request.data['url']

            try:
                QRCode.objects.get(name=name)
                return Response({'error': 'QR Code with this name already exists'})
            except QRCode.DoesNotExist:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.ERROR_CORRECT_L,
                    box_size=10,
                    border=4
                )
                qr.add_data(url)
                qr.make(fit=True)

                img = qr.make_image(back_color=(255, 255, 255), fill_color=(16, 16, 16))

                file_name = random.randint(111111111, 999999999)
                file_name = str(file_name) + '.png'
                path = os.path.join(BASE_DIR, 'qrcodes', 'tmp', file_name)
                img.save(path)
                instance = QRCode(
                    owner_id=request.user.id,
                    name=name,
                    description=description,
                    url=url
                )

                path = Path(path)
                with path.open(mode='rb') as f:
                    instance.file = File(f, name=file_name)
                    instance.save()

                os.remove(path)

                serializer = QRCodeSerializer(instance)
                return Response({'success': 'You have successfully generated QR Code', 'data': serializer.data})
        except KeyError:
            return Response({'error': 'Missing name or description or url'})


class QRCodeListView(APIView):
    def get(self, request):
        try:
            qrcodes = QRCode.objects.filter(owner_id=request.user.id)
            serializer = QRCodeSerializer(qrcodes, many=True)
            return Response(serializer.data)
        except QRCode.DoesNotExist:
            return Response({'error': 'You have no QR Codes'})


class QRCodeDetailView(APIView):
    def get(self, request, pk=None):
        try:
            qrcode = QRCode.objects.get(pk=pk, owner_id=request.user.id)
            serializer = QRCodeSerializer(qrcode)
            return Response(serializer.data)
        except QRCode.DoesNotExist:
            return Response({'error': 'QR Code does not exist'})