from django.urls import path
from .views import ascii_art_view

urlpatterns = [
    #path('ascii-art-image/', ascii_art_view, name='ascii_art_image'),
    path('', ascii_art_view, name='ascii_art_image'),
]