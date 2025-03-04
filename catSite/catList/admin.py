from django.contrib import admin
from .models import Cat
from image_cropping import ImageCroppingMixin

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name_es', 'age', 'breed_es')  # Default to Spanish
    fields = (
        'name_es', 'name_en',
        'sexo_es', 'sexo_en',
        'breed_es', 'breed_en',
        'description_es', 'description_en',
        'personality_traits_es', 'personality_traits_en',
        'image', 'cropping'
    )

# admin.site.register(Cat, CatAdmin)