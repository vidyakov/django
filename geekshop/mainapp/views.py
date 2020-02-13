from django.shortcuts import render
from .models import ProductCategory, Product, Contacts


def main(request):
    content = {
        'title': 'главная',
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    content = {
        'title': 'контакты',
        'contacts': Contacts.objects.all()
    }
    return render(request, 'mainapp/contact.html', content)


def product(request, pk=None):
    content = {
        'title': 'продукты',
        # Похожие товары
        'products': [
            {
                'src': '/img/product-11.jpg',
                'title': 'Стул повышенного качества',
                'second_title': 'Не оторваться.'
            },
            {
                'src': '/img/product-21.jpg',
                'title': 'Стул повышенного качества',
                'second_title': 'Не оторваться.'
            },
            {
                'src': '/img/product-31.jpg',
                'title': 'Стул повышенного качества',
                'second_title': 'Не оторваться.'
            },
        ],
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'mainapp/products.html', content)
