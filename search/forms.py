from django import forms

class SearchForm(forms.Form):
    year = forms.CharField(max_length=20, label="Year")
    make = forms.CharField(max_length=200, label="Make")
    model = forms.CharField(max_length=200, label="Model")
    mileage = forms.IntegerField(label="Mileage", required=False)
