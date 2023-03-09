from django.db import models
from django.utils import timezone

# Create your models here.

class Entry(models.Model):
    """
    In addition to title, content, and date_created, Django will automatically add id as a unique primary key. 
    The string representation of an entry with the primary key 1 would be Entry object (1) by default. 
    When you add .__str__(), you can customize what is shown instead. 
    For a diary entry, the title is a better string representation.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        """
        The Meta class is a way to provide additional information about the model.
        In this case, we're telling Django to use 'Entries' instead of 'Entrys' when it needs to refer to more than one entry.
        """
        verbose_name_plural = 'entries'