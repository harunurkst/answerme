from django.shortcuts import render

from .models import Tag, Category

def all_tags(request):
    tags = Tag.objects.all()

    context = {
        'tags':tags,
    }
    return render(request, 'tagory/index.html', context)


def all_categories(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'tagory/index.html', context)