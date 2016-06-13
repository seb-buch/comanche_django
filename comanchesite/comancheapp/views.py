from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login

from . import __version__


def get_common_context(request):
    context = {
        'version': __version__
    }

    try:
        if request.POST["what"] == "login":
            user = authenticate(username=request.POST["username"], password=request.POST["password"])
            if user is None:
                context["login_warning"] = "invalid username/password!"
            elif user.is_active:
                login(request, user)
            else:
                context["login_warning"] = "your acoount is disabled!"
    except KeyError:
        pass

    return context


def index(request):
    context = get_common_context(request)
    return render(request, "comancheapp/index.html", context)


def equilibration(request):
    context = get_common_context(request)
    return render(request, "comancheapp/equilibration.html", context)


def insertion(request):
    context = get_common_context(request)
    return render(request, "comancheapp/insertion.html", context)


def umbrella(request):
    context = get_common_context(request)
    return render(request, "comancheapp/umbrella.html", context)


def lipids(request):
    context = get_common_context(request)
    return render(request, "comancheapp/lipids.html", context)


def membranes(request):
    context = get_common_context(request)
    return render(request, "comancheapp/membranes.html", context)


def forcefields(request):
    context = get_common_context(request)
    return render(request, "comancheapp/forcefields.html", context)


def jobs(request):
    context = get_common_context(request)
    return render(request, "comancheapp/jobs.html", context)


def logout(request):
    logout(request)
    context = get_common_context(request)
    return render(request, "comancheapp/in.html", context)
