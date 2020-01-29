from django.shortcuts import render


def authors(request):
    context = {}
    return render(request, "authors/authors.html", context=context)
