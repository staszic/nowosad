from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Plant


# Create your views here.
def index(request):
    plants_list = Plant.objects.order_by('category', 'plant_name')
    paginator = Paginator(plants_list, 12)
    page = request.GET.get('page')
    plants = paginator.get_page(page)
    context = {'plants_list': plants}
    return render(request, 'plants/index.html', context)


def detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})