from django.shortcuts import render, get_object_or_404
from .models import Category, Word


# Create your views here.
def category_list(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'category_list.html', {'categories': categories})


def category_children(request, pk):
    parent_category = get_object_or_404(Category, pk=pk)
    children = parent_category.children.all()
    return render(request, 'category_list.html', {'categories': children})
