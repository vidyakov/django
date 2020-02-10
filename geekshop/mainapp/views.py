from django.shortcuts import render


def main(request):
    content = {
        'title': 'главная',
        'products': [
            {
                'src': '/img/product-1.jpg',
                'title': 'Отличный стул',
                'second_title': 'Расположитесь комфортно. '
            },
            {
                'src': '/img/product-2.jpg',
                'title': 'Стул повышенного качества',
                'second_title': 'Не оторваться. '
            }
        ]
    }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    content = {
        'title': 'контакты',
        'contacts': [
            {
                'city': 'Москва',
                'phone': '+7-888-888-8888',
                'email': 'info@geekshop.ru',
                'address': 'В пределах МКАД'
            },
            {
                'city': 'Москва',
                'phone': '+7-888-888-8888',
                'email': 'info@geekshop.ru',
                'address': 'В пределах МКАД'
            },
            {
                'city': 'Москва',
                'phone': '+7-888-888-8888',
                'email': 'info@geekshop.ru',
                'address': 'В пределах МКАД'
            },
        ]
    }
    return render(request, 'mainapp/contact.html', content)


def product(request):
    content = {
        'title': 'продукты',
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
        'categories': [
            {
                'src': 'products_all',
                'name': 'все'
            },
            {
                'src': 'products_home',
                'name': 'дом'
            },
            {
                'src': 'products_office',
                'name': 'офис'
            },
            {
                'src': 'products_modern',
                'name': 'модерн'
            },
            {
                'src': 'products_classic',
                'name': 'классика'
            },
        ]
    }
    return render(request, 'mainapp/products.html', content)
