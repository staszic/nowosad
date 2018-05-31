from django.shortcuts import render, get_object_or_404
from .models import Plant, Category


# Create your views here.
def index(request):
    categories = Category.objects.order_by('category_name')
    plants_by_cat = {}
    plants = Plant.objects.order_by('category', 'plant_name')
    for cat in categories:
        plants_by_cat[cat] = plants.filter(category=cat)
    context = {'categories': categories, 'plants': plants_by_cat}
    return render(request, 'plants/index.html', context)


def detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})