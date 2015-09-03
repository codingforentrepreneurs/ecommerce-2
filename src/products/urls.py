from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from .views import ProductDetailView, ProductListView,VariationListView 

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    #url(r'^$', 'products.views.product_list', name='products'),
    url(r'^$', ProductListView.as_view(), name='products'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),
    #url(r'^(?P<id>\d+)', 'products.views.product_detail_view_func', name='product_detail_function'),
]