from django.db import models

# Create your models here.

class DataStore(models.Model):

    vin=models.CharField(max_length=30, null=True)
    year=models.CharField(max_length=6, null=True, db_index=True)
    make=models.CharField(max_length=200, null=True, db_index=True)
    model=models.CharField(max_length=200, null=True, db_index=True)
    trim=models.CharField(max_length=300, null=True)
    dealer_name=models.CharField(max_length=200, null=True)
    dealer_street=models.CharField(max_length=300, null=True)
    dealer_city=models.CharField(max_length=200, null=True)
    dealer_state=models.CharField(max_length=200, null=True)
    dealer_zip=models.CharField(max_length=20, null=True)
    listing_price=models.CharField(max_length=200, null=True)
    listing_mileage=models.CharField(max_length=200, null=True)
    used=models.CharField(max_length=200, null=True)
    certified=models.CharField(max_length=200, null=True)
    style=models.CharField(max_length=500, null=True)
    driven_wheels=models.CharField(max_length=200, null=True)
    engine=models.CharField(max_length=200, null=True)
    fuel_type=models.CharField(max_length=200, null=True)
    exterior_color=models.CharField(max_length=200, null=True)
    interior_color=models.CharField(max_length=200, null=True)
    seller_website=models.CharField(max_length=200, null=True)
    first_seen_date=models.CharField(max_length=200, null=True)
    last_seen_date=models.CharField(max_length=200, null=True)
    dealer_vdp_last_seen_date=models.CharField(max_length=100, null=True)
    listing_status=models.CharField(max_length=200, null=True)
    
    class Meta:
        db_table='data_store'
        indexes = [
            models.Index(fields=['year', 'make', 'model']),  # Compound index on 'year', 'make', and 'model'
        ]