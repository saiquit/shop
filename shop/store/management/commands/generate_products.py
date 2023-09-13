import random
from django.core.management.base import BaseCommand
from faker import Faker
from store.models import Category, Product, Variation, Tag  # Replace with your actual models

class Command(BaseCommand):
    help = 'Generate fake categories and products'

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_categories = 4  # Number of categories to create
        max_products_per_category = 2  # Maximum number of products per category
        # Tag.objects.create(name='Featured')
        for _ in range(num_categories):
            category = Category.objects.create(
                name=fake.word(),
                description=fake.sentence(),
            )

            num_products = random.randint(1, max_products_per_category)
            for _ in range(num_products):
                product = Product.objects.create(
                    category=category,
                    active=fake.boolean(),
                    name=fake.sentence(),
                    description=fake.sentence(),
                )
                for _ in range(2):
                    Variation.objects.create(
                    products=product,
                    price=random.uniform(100.0, 1000.0),
                    sale=random.uniform(10.0, 100.0),
                    stock=fake.random_int(10,100),
                    color=fake.word(),
                    size=fake.random_int(250,1000),
                    )

        self.stdout.write(self.style.SUCCESS('Successfully generated fake categories and products'))
