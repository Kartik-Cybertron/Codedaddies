from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # then uses the path in function then inside check path and if blank
    # then goes for the another keyword arguments and call it
    path('new_search', views.new_search, name="new_search"),
]
