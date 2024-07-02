from django.shortcuts import render, get_object_or_404
from .models import Category, Word


def category_view(request, pk=None):
    words = None
    category = None
    if pk:
        category = get_object_or_404(Category, id=pk)
        category_children = category.children.all()
        if not category_children:
            words = category.words.all()
    else:
        category_children = Category.objects.filter(parent__isnull=True)

    return render(request, 'category_list.html',
                  context={
                      'category': category,
                      'child_category': category_children,
                      'words': words
                  })


def word_detail_view(request, slug):
    detail = get_object_or_404(Word, slug=slug)
    name = detail.name
    image = detail.image
    video = detail.video
    description = detail.description
    context = {'name': name, 'image': image, 'video': video, 'description': description}
    return render(request, 'word_detail.html', context)
