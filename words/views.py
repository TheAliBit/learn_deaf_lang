from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from main.models import Profile
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
                      'words': words,
                  })


def word_detail_view(request, slug):
    detail = get_object_or_404(Word, slug=slug)
    profile: Profile = request.user
    context = {'word': detail, 'profile': profile}
    return render(request, 'word_detail.html', context)


@login_required
def like_word(request, slug):
    word = get_object_or_404(Word, slug=slug)
    profile: Profile = request.user
    profile.liked_words.add(word)
    return redirect(reverse(word_detail_view, kwargs={'slug': slug}))


@login_required
def unlike_word(request, slug):
    word = get_object_or_404(Word, slug=slug)
    profile: Profile = request.user
    profile.liked_words.remove(word)
    return redirect(reverse(word_detail_view, kwargs={'slug': slug}))
