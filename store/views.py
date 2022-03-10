from django.shortcuts import render
from store.forms.product_forms import FilterForm
from store.services.product_service import ProductService


def category_view(request, name):
    product_service = ProductService()
    products = product_service.find_by_category(name)

    return render(request, "store/category.html",
                  {'products': products,
                   'category_name': name})

def filter_view(request):
    product_service = ProductService()
    form = FilterForm(request.GET)

    if form.is_valid():
        name = form.cleaned_data['name']
        category = form.cleaned_data['category']
        order_by = form.cleaned_data['order_by']
        only_in_stock = form.cleaned_data['only_in_stock']

        products = product_service.filter(name, category, only_in_stock, order_by)

    else:
        products = product_service.get_in_stock()

    return render(request, "store/filter.html", {'form': form, 'products': products})





