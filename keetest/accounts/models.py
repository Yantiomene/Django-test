from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
# Create your models here.

phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birthday = models.DateField()
    phonenumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    image = models.ImageField(upload_to='accounts_images/', null=True, blank=True)


    def __str__(self):
        return self.user.username

    #def save(self, *args, **kwargs):
    #    super().save(*args, **kwargs)

    #img = Image.open(self.image.path)
    #if img.height > 300 or img.width > 300:
    #    output_size = (300, 300)
    #    img.thumbnail(output_size)
    #    img.save(self.image.path)
    