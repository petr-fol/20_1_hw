from django.core.management import BaseCommand


class fill_db(BaseCommand):
    help = 'вставить начальные значения для базы данных'

    def handle(self, *args, **options):
        from catalog.models import Product, Category

        Product.objects.all().delete()
        Category.objects.all().delete()

        Product.objects.create(name='продукт 1', price=100, category='категория 1')
        Product.objects.create(name='продукт 2', price=100, category='категория 2')
        Product.objects.create(name='продукт 3', price=100, category='категория 2')

        Category.objects.create(name='категория 1', description='описание категории 1')
        Category.objects.create(name='категория 2', description='описание категории 2')

        self.stdout.write(self.style.SUCCESS('Успешно вставлены начальные значения для базы данных'))
