from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    