from django.db import models
from image_cropping import ImageRatioField

class Cat(models.Model):
    SEX_CHOICES_es = [
        ('macho', 'Macho'),  # Male
        ('hembra', 'Hembra'),  # Female
    ]
    SEX_CHOICES_en = [
        ('male', 'Male'),  # Male
        ('female', 'Female'),  # Female
    ]

    # Name
    name_es = models.CharField(max_length=100, default="joe", verbose_name="Nombre (ES)")
    name_en = models.CharField(max_length=100, default="joe",verbose_name="Name (EN)", blank=True, null=True)

    # Age (No need to translate)
    age = models.PositiveIntegerField(default=0)  # or any sensible default

    # Sexo (Gender)
    sexo_es = models.CharField(max_length=6, choices=SEX_CHOICES_es, default='macho', verbose_name="Sexo (ES)")
    sexo_en = models.CharField(max_length=6, choices=SEX_CHOICES_en, default='male', verbose_name="Gender (EN)", )

    # Breed
    breed_es = models.CharField(max_length=100, default="joe", verbose_name="Raza (ES)")
    breed_en = models.CharField(max_length=100, default="joe", verbose_name="Breed (EN)")

    # Description
    description_es = models.TextField(default="joe", verbose_name="Descripción (ES)")
    description_en = models.TextField(default="joe", verbose_name="Description (EN)")

    # Image
    image = models.ImageField(upload_to='cats/')
    cropping = ImageRatioField('image', '400x500')  # Image cropping

    # Personality Traits
    personality_traits_es = models.CharField(max_length=100, default="joe", verbose_name="Rasgos de personalidad (ES)")
    personality_traits_en = models.CharField(max_length=100, default="joe", verbose_name="Personality Traits (EN)")

    def get_field(self, field_name, lang):
        """Returns the correct field value based on language."""
        return getattr(self, f"{field_name}_{lang}", getattr(self, f"{field_name}_es", ""))

    def __str__(self):
        return self.name_es  # Default to Spanish in Django Admin