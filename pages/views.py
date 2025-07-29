from django.shortcuts import render, get_object_or_404
from . models import Page
# Create your views here.
def page(request):
    all_pages = Page.objects.all()
    return render(request, 'pages/page_details.html',{'pages':all_pages})
def page_detail(request,slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request,'pages/page_details.html', {'page': page})