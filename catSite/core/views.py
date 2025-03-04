from django.shortcuts import render
from catList.models import Cat  # Importing from the 'cats' app

import os
from django.conf import settings

def home(request):
    # Retrieve all cats
    cats = Cat.objects.all()

    # Path to the 'fotoPrincipal' folder inside the 'media' directory
    folder_path = os.path.join(settings.MEDIA_ROOT, 'fotoPrincipal')
    first_image = None

    # Get the first image in the folder
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = sorted(os.listdir(folder_path))  # Sort files to ensure consistent order
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                first_image = f'fotoPrincipal/{file}'  # Path relative to MEDIA_URL
                break

    # Pass the first image and cats to the template
    return render(request, 'home.html', {
        'cats': cats,
        'first_image': first_image,
    })
def about(request):
    return render(request, "nuestraFamilia.html")

def history(request):
    return render(request, "historia.html")

