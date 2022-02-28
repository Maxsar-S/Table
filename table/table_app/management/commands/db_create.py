from django.core.management.base import BaseCommand

from table_app.models import Cell
import random
from datetime import datetime as dt
from datetime import timedelta


class Command(BaseCommand):
    help = 'Create cells for testing'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        start_dt = dt.strptime('01.01.2021', '%d.%m.%Y')
        end_dt = dt.strptime('27.02.2022', '%d.%m.%Y')

        Cell.objects.all().delete()
        count = options['count']
        for i in range(count):
            date = (start_dt + timedelta(random.randint(0, (end_dt - start_dt).days))).date()
            cell = Cell.objects.create(
                date=date,
                name=f'fname{i}',
                quantity=i * i,
                distance=i * i
            )
            print(f'Article {cell} created')
