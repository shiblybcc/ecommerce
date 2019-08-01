from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Product

class ProductListView(ListView):
    qs = Product.objects.all()
    template_name = 'products/list.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context

# above class based view and below function based view are same
# def product_list_view(request):
#     qs = Product.objects.all()
#     context = {
#         'object_list': qs
#     }
#     return render(request, 'product/product_list_view.html', context)


class ProductDetailView(DetailView):
    qs = Product.objects.all()
    template_name = 'products/detail.html'