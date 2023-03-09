from django.contrib import admin
from .models import Entry


# Register your models here.
# To also see the Entry model in the Django admin site, you need to register it in entries/admin.py:

admin.site.register(Entry)