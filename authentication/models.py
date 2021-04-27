from typing import final
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='profile_img')


    def save(self):
        super().save()
        imag = Image.open(self.img.path)
        
        if imag.height > 270 or imag.width > 270:
            final_output = (270, 1270)
            imag.thumbnail(final_output)
            imag.save(self.img.path)
            