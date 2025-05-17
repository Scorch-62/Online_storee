from django.core.management.base import BaseCommand
from Catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        category = Category.objects.get_or_create(name='Роман', description='')

        product = [{'title': 'Лунное затмение', 'publication_date': '2020-5-02', 'category': category},
                   {'title': 'Смертельная пуля', 'publication_date': '2020-5-02', 'category': category},
                   ]

        for product_date in product:
            product, created = Product.objects.get_or_create(**product_date)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.title}'))

