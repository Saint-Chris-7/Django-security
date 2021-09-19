from django.db import models
from django.db.models.base import Model
from django.db import models
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw
from django.core.files import File



# Create your models here.
class User_data(models.Model):
    os_list= (("windows","Windows"),("harmony","harmony"),("ubuntu","ubuntu"),("ios","ios"),("android","android"),("linux","linux"))
    qr_code = models.ImageField(upload_to="qr_codes",help_text="student image",blank=True)
    first_name = models.CharField(max_length=19,help_text="student first name ")
    last_name = models.CharField(max_length=19,help_text="student last name")
    email = models.EmailField(help_text="student email")
    reg_no = models.CharField(max_length=16,help_text="registration number ")
    gadget_brand = models.CharField(max_length=15,help_text="e.g. hp")
    gadget_model = models.CharField(max_length=15,help_text="folio 9470")
    gadget_serial = models.CharField(max_length=15,help_text="CNU4149***")
    gadget_os = models.CharField(max_length=8,choices=os_list)
    reg_date= models.DateField(auto_now_add=True)
    
   
    def __str__(self):
        return f'{self.reg_no} {self.first_name} {self.last_name} '

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.reg_no)
        canvas = Image.new("RGB",(290,290),"white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f"qrcode-{self.reg_no}.png"
        buffer = BytesIO()
        canvas.save(buffer,"Png")
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)
    class Meta:
        ordering=["-first_name"]



