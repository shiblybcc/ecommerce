from django.views.generic import ListView, DetailView
from django.shortcuts import render, Http404, get_object_or_404

from .models import Product


class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()

    template_name = 'products/featured-detail.html'


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

# above class based view and below function based view are same
# def product_list_view(request):
#     qs = Product.objects.all()
#     context = {
#         'object_list': qs
#     }
#     return render(request, 'product/product_list_view.html', context)


class ProductFeaturedDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = get_object_or_404(Product, slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Product doesn't exists")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404('something went wrong')
        return instance


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context

    # def get_object(self, queryset=None):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("Product doesn't exists")
    #     return instance

    # same as get_object above
    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)
