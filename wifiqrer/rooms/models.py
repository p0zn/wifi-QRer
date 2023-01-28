from django.db import models
import wifi_qrcode_generator
from io import BytesIO
from django.core.files.base import ContentFile

class Rooms(models.Model):
    name = models.CharField(max_length=50)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self,*args,**kwargs):
        if not self.qr_code:
            room_name = self.name
            qr_code = wifi_qrcode_generator.wifi_qrcode(
                    f'{room_name}', False, 'WPA', 'your-wifi-key')
            
            file_name = f'qr-code-{room_name}.png'
            buffer = BytesIO()
            qr_code.save(buffer,format = 'PNG')

            self.qr_code = ContentFile(buffer.getvalue(), file_name)



        super().save(*args,**kwargs)