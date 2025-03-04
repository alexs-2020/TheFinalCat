from django.contrib import admin
from django.contrib import admin
from .models import FotoPrincipal
from image_cropping import ImageCroppingMixin



# Register your models here.
@admin.register(FotoPrincipal)
class FotoPrincipal(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'img')