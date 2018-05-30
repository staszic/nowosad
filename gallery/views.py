from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Image

# Create your views here.
def index(request):
    images_list = Image.objects.order_by('alt_title')
    paginator = Paginator(images_list, 12)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    context = {'images_list': images}
    return render(request, 'gallery/index.html', context)