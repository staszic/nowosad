from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Image

# Create your views here.
def index(request):
    images_list = Image.objects.order_by('alt_title')
    context = {'images_list': images_list}
    return render(request, 'gallery/index.html', context)