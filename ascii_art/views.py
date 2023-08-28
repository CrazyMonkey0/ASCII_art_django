from django.shortcuts import render
from .ASCII_art import convert_to_ascii


def ascii_art_view(request):
    ascii_art_image = None
    # Sending an image and its loading
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_image = request.FILES["image"]
        ascii_art_image = convert_to_ascii(uploaded_image)

        # Displaying ASCII art image
        return render(request, 'ascii_art/image_to_ascii_done.html', {'ascii_art_image': ascii_art_image})

    return render(request, 'ascii_art/image_to_ascii.html', {'ascii_art_image': ascii_art_image})
