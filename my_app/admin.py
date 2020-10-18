from django.contrib import admin
from .models import Search

# Register your models here.
admin.site.register(Search)  # to register the search to admin and make migrations then migrate to see changes
