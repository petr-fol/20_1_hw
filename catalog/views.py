from django.shortcuts import render

# Create your views here.
from .models import Product, Category, Contact


# def latest_products(request):
#     products = Product.objects.order_by('-id')[:5]
#     context = {
#         'products': products
#     }
#     print(context)
#     return render(request, 'catalog/templates/latest_products.html', context)
#
#
# def contact_view(request):
#     contacts = Contact.objects.all()
#     print(contacts)
#     return render(request, 'catalog/templates/contact.html', {'contacts': contacts})
