from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')


def sobrenos(request):
    return render(request, 'sobrenos.html')


def erro404(request, execption):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='Text/html; charset=utf8', status=404)


def erro500(request, execption):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='Text/html; charset=utf8', status=500)
