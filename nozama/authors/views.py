from django.shortcuts import render

from .models import Author


def authors(request):
    authors_list = Author.objects.all()
    context = {
        "authors_list": authors_list,
    }
    return render(request, "authors/authors.html", context=context)
