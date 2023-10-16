from django.shortcuts import render
from django.db.models import Q, F, Sum, Value, CharField, FloatField
from django.db.models.functions import Concat, Cast, Abs

from .models import DataStore
from .data_model import get_regression_val
from .forms import SearchForm
import re

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            year, make, model = form.cleaned_data['year'], form.cleaned_data['make'], form.cleaned_data['model']
            make = re.sub(r'\s+', ' ', make)
            model = re.sub(r'\s+', ' ', model)
            inp_mileage = form.cleaned_data['mileage']

            listings = DataStore.objects.filter(
                year=year,make=make, model=model
            )
            if not listings.exists():
                return render(request, 'search.html', {
                    'form': form,
                    'estimated_price': 'Please check your inputs - No Data available for this combination!',
                    'sample_listings': [],
                })

            if inp_mileage:
                listings = listings.exclude(
                    listing_mileage = "nan"
                ).exclude(
                    listing_price = "nan"
                ).annotate(
                    mileage=Cast(F('listing_mileage'), FloatField()),
                    price=Cast(F('listing_price'), FloatField())
                )

                modeling_data = list( listings.values_list('mileage', 'price') )
                estimated_price = get_regression_val(modeling_data, float(inp_mileage))
                # listings = listings.filter(listing_mileage__lte=mileage)  #think of a different logic for this
                # sample_listings = listings.annotate(abs_mileage_diff=Abs(F('mileage') - Value(inp_mileage))).order_by('abs_mileage_diff')[:100]


            else:
                estimated_price = calculate_estimated_price(listings)
            
            sample_listings = listings[:100]

            return render(request, 'search.html', {
                'form': form,
                'estimated_price': max(estimated_price, 0.00),
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
