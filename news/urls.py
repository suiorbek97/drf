from django.urls import path
from .views import (
    index)
    # add_view)

urlpatterns = [
    path('index/', index),
    # path('add/', add_view),
]