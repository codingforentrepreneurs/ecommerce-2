from django.shortcuts import render
from django.views.generic.edit import FormView
# Create your views here.

from .forms import AddressForm

class AddressSelectFormView(FormView):
	form_class = AddressForm
	template_name = "orders/address_select.html"