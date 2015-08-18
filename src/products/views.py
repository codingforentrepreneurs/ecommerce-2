from  django.views.generic.detail import DetailView
from django.shortcuts import render

# Create your views here.


from .models import Product


class ProductDetailView(DetailView):
	model = Product


def product_detail_view_func(request, id):
	product_instance = Product.objects.get(id=id)
	template = "products/product_detial.html"
	context = {	
		"object": product_instance
	}
	return render(request, template, context)