from django.shortcuts import render
from django.db.models import Q, F, Sum, Value, CharField
from django.db.models.functions import Concat
from .models import DataStore
from .forms import SearchForm
import re

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            year, make, model = form.cleaned_data['year'], form.cleaned_data['make'], form.cleaned_data['model']
            make = re.sub(r'\s+', ' ', make)
            model = re.sub(r'\s+', ' ', model)
            mileage = form.cleaned_data['mileage']

            listings = DataStore.objects.filter(
                year=year,make=make, model=model
            )

            if mileage:
                listings = listings.filter(mileage__lte=mileage)

            estimated_price = calculate_estimated_price(listings)
            sample_listings = listings[:100]

            return render(request, 'search.html', {
                'form': form,
                'estimated_price': estimated_price,
                'sample_listings': sample_listings,
            })
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})

def calculate_estimated_price(listings):
    total_price = listings.aggregate(total=Sum('listing_price'))['total']
    if listings.count() > 0:
        return round(total_price / listings.count(), -2)
    else:
        return 0
