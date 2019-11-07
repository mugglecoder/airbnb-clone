from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models, forms


class Homeview(ListView):

    """ homeview definition """

    model = models.Room
    paginate_orphans = 5
    paginate_by = 10
    context_object_name = "rooms"


class RoomDetail(DetailView):

    model = models.Room


def search(request):

    form = forms.SearchForm()

    return render(request, "rooms/search.html", {"form": form})
