from django.http import HttpResponse
from django.template import loader

from . import __version__


def get_common_context():
    return {
        'version': __version__
    }


def index(request):
    template = loader.get_template('comancheapp/index.html')
    context = get_common_context()
    return HttpResponse(template.render(context, request))


def equilibration(request):
    template = loader.get_template('comancheapp/equilibration.html')
    context = get_common_context()
    return HttpResponse(template.render(context, request))


def insertion(request):
    template = loader.get_template('comancheapp/insertion.html')
    context = get_common_context()
    return HttpResponse(template.render(context, request))


def umbrella(request):
    template = loader.get_template('comancheapp/umbrella.html')
    context = get_common_context()
    return HttpResponse(template.render(context, request))


def lipids(request):
    template = loader.get_template('comancheapp/lipids.html')
    context = get_common_context()
    return HttpResponse(template.render(context, request))


def membranes(request):
    template = loader.get_template('comancheapp/membranes.html')
    context = get_common_context()
    return HttpResponse(template.render(context, request))


def forcefields(request):
    template = loader.get_template('comancheapp/forcefields.html')
    context = get_common_context()
    return HttpResponse(template.render(context, request))


def jobs(request):
    template = loader.get_template('comancheapp/jobs.html')
    context = get_common_context()
    return HttpResponse(template.render(context, request))
