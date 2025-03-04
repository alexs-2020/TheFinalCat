from django.utils.translation import get_language
from django.shortcuts import render, get_object_or_404
from .models import Cat

def catList(request):
    cats = Cat.objects.all()
    selected_cat = None
    language_code = get_language()  # Get the active language

    if 'selected_cat' in request.GET:
        selected_cat_id = request.GET.get('selected_cat')
        selected_cat = get_object_or_404(Cat, id=selected_cat_id)

    return render(request, 'catList.html', {
        'cats': cats,
        'selected_cat': selected_cat,
        'LANGUAGE_CODE': language_code,  # Pass the active language to the template
    })

def machos(request):
    language = get_language()

    if language == "en":
        cats = Cat.objects.filter(sexo_en="male")
    else:
        cats = Cat.objects.filter(sexo_es="macho")

    selected_cat = None

    if 'selected_cat' in request.GET:
        selected_cat_id = request.GET.get('selected_cat')
        selected_cat = get_object_or_404(Cat, id=selected_cat_id)
        print(f"Selected cat: {selected_cat}")  # ✅ Debugging: Check if selected_cat is found

    return render(request, 'catList.html', {
        'cats': cats,
        'selected_cat': selected_cat,
    })
def hembras(request):
    language = get_language()

    if language == "en":
        cats = Cat.objects.filter(sexo_en="female")
    else:
        cats = Cat.objects.filter(sexo_es="hembra")

    selected_cat = None

    if 'selected_cat' in request.GET:
        selected_cat_id = request.GET.get('selected_cat')
        selected_cat = get_object_or_404(Cat, id=selected_cat_id)
        print(f"Selected cat: {selected_cat}")  # ✅ Debugging: Check if selected_cat is found

    return render(request, 'catList.html', {
        'cats': cats,
        'selected_cat': selected_cat,
    })























# from django.shortcuts import render, get_object_or_404
#
# from catList.models import Cat
# #
# # def catList(request):
# #     cats = Cat.objects.all()
# #     selected_cat = None
# #
# #     # Check if a specific cat is selected
# #     if 'selected_cat' in request.GET:
# #         selected_cat_id = request.GET.get('selected_cat')
# #         selected_cat = get_object_or_404(Cat, id=selected_cat_id)
# #
# #     return render(request, 'catList.html', {
# #         'cats': cats,
# #         'selected_cat': selected_cat,
# #     })
# #
# # def machos(request):
# #     cats = Cat.objects.filter(sexo='macho')
# #     print(cats)  # Log to console
# #     return render(request, 'catList.html', {'cats': cats})
# #
# # def hembras(request):
# #     cats = Cat.objects.filter(sexo='hembra')
# #     return render(request, 'catList.html', {'cats': cats})
#
#
# from django.shortcuts import render, get_object_or_404
# from .models import Cat
#
# def catList(request):
#     cats = Cat.objects.all()
#     selected_cat = None
#
#     # Check if a specific cat is selected
#     if 'selected_cat' in request.GET:
#         selected_cat_id = request.GET.get('selected_cat')
#         selected_cat = get_object_or_404(Cat, id=selected_cat_id)
#
#     return render(request, 'catList.html', {
#         'cats': cats,
#         'selected_cat': selected_cat,
#     })
#
# def machos(request):
#     cats = Cat.objects.filter(sexo='macho')
#     selected_cat = None
#
#     # Check if a specific cat is selected
#     if 'selected_cat' in request.GET:
#         selected_cat_id = request.GET.get('selected_cat')
#         selected_cat = get_object_or_404(Cat, id=selected_cat_id)
#
#     return render(request, 'catList.html', {
#         'cats': cats,
#         'selected_cat': selected_cat,
#     })
#
# def hembras(request):
#     cats = Cat.objects.filter(sexo='hembra')
#     selected_cat = None
#
#     # Check if a specific cat is selected
#     if 'selected_cat' in request.GET:
#         selected_cat_id = request.GET.get('selected_cat')
#         selected_cat = get_object_or_404(Cat, id=selected_cat_id)
#
#     return render(request, 'catList.html', {
#         'cats': cats,
#         'selected_cat': selected_cat,
#     })