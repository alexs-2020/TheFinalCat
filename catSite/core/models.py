import os
from django.db import models
from django.dispatch import receiver

# Create your models here.

class FotoPrincipal(models.Model):
    name = models.CharField(max_length=120)
    img = models.ImageField(upload_to='fotoPrincipal/')

    # Signal to delete the file when the FotoPrincipal instance is deleted
@receiver(models.signals.post_delete, sender=FotoPrincipal)
def delete_foto_principal_file(sender, instance, **kwargs):
    print(instance)
    if instance.img and os.path.isfile(instance.img.path):
        os.remove(instance.img.path)