from django.db import models


# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)  # to set char limit to 500 for var
    created = models.DateTimeField(auto_now=True)  # to set data and time automatically in var

    def __str__(self):  # To show data directly in the list of admin searches or
        return '{}'.format(self.search)  # Else it shows object of the search

    class Meta:
        verbose_name_plural = 'Searches'  # to changes the verb in the my app dialog box from search to searches
