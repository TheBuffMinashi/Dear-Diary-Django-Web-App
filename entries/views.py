from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry

# Create your views here.
class EntryListView(ListView):
    model = Entry

    """
    Entry.objects.all() on line 15 would return all entries ordered by their primary key.
    Enhancing it with .order_by("-date_created") will return your entries in ascending order, 
    with the newest entry on top of the list.
    """
    queryset = Entry.objects.all().order_by("-date_created")

class EntryDetailView(DetailView):
    model = Entry