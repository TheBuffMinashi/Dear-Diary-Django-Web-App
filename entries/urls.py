from django.urls import path
from . import views

""""
The path() function on lines 9 and 10 must have at least two arguments:

1. A route string pattern, which contains a URL pattern
2. The reference to a view, which is an as_view() function for class-based views

"""


urlpatterns = [
    path("", views.EntryListView.as_view(), name="entry-list"),
    path("entry/<int:pk>", views.EntryDetailView.as_view(), name="entry-detail"),
]