from django.core.management.base import BaseCommand
import pandas as pd
from search.models import DataStore

class Command(BaseCommand):
    help = 'Import data from a text file to the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the text file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        
        try:
            chunk_size = 20000 
            for chunk in pd.read_csv(file_path, sep='|', chunksize=chunk_size):
                records = []
                for _, row in chunk.iterrows():
                    record = DataStore(
                        vin=row['vin'],
                        year=row['year'],
                        make=row['make'],
                        model=row['model'],
                        trim=row['trim'],
                        dealer_name=row['dealer_name'],
                        dealer_street=row['dealer_street'],
                        dealer_city=row['dealer_city'],
                        dealer_state=row['dealer_state'],
                        dealer_zip=row['dealer_zip'],
                        listing_price=row['listing_price'],
                        listing_mileage=row['listing_mileage'],
                        used=row['used'],
                        certified=row['certified'],
                        style=row['style'],
                        driven_wheels=row['driven_wheels'],
                        engine=row['engine'],
                        fuel_type=row['fuel_type'],
                        exterior_color=row['exterior_color'],
                        interior_color=row['interior_color'],
                        seller_website=row['seller_website'],
                        first_seen_date=row['first_seen_date'],
                        last_seen_date=row['last_seen_date'],
                        dealer_vdp_last_seen_date=row['dealer_vdp_last_seen_date'],
                        listing_status=row['listing_status'],
                    )
                    records.append(record)
                DataStore.objects.bulk_create(records)
                
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing data: {str(e)}'))
