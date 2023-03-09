from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Entry


# Create your views here.
class LockedView(LoginRequiredMixin):
    login_url = "admin:login"
class EntryListView(LockedView, ListView):
    model = Entry

    """
    Entry.objects.all() on line 15 would return all entries ordered by their primary key.
    Enhancing it with .order_by("-date_created") will return your entries in ascending order, 
    with the newest entry on top of the list.
    """
    queryset = Entry.objects.all().order_by("-date_created")

class EntryDetailView(LockedView, DetailView):
    model = Entry

class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new entry was created!"

class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.entry.id}
        )

class EntryDeleteView(LockedView, SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)