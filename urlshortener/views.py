from django.shortcuts import render, redirect
from .forms import URLForm
import random
import string
from .models import URL

def shorten_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            # generate shortened url
            short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            # save to database
            return render(request, 'urlshortener/shorten_url.html', {'form': form, 'shortened_url': short_url})
    else:
        form = URLForm()
    return render(request, 'urlshortener/shorten_url.html', {'form': form})

def success(request):
    return render(request, 'urlshortener/success.html')
