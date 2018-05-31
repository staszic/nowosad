from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Plant, Category


# Create your views here.
def index(request):
    categories = Category.objects.order_by('category_name')
    plants = Plant.objects.order_by('category', 'plant_name')
    context = {'categories': categories, 'plants': plants}
    return render(request, 'plants/index.html', context)


def detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})