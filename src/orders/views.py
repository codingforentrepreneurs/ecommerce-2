from django.shortcuts import render
from django.views.generic.edit import FormView
# Create your views here.

from .forms import AddressForm
from .models import UserAddress

class AddressSelectFormView(FormView):
	form_class = AddressForm
	template_name = "orders/address_select.html"

	def get_form(self, *args, **kwargs):
		form = super(AddressSelectFormView, self).get_form(*args, **kwargs)
		form.fields["billing_address"].queryset = UserAddress.objects.filter(
				user__email=self.request.user.email,
				type='billing',
			)
		form.fields["shipping_address"].queryset = UserAddress.objects.filter(
				user__email=self.request.user.email,
				type='shipping',
			)
		return form

	def form_valid(self, *args, **kwargs):
		form = super(AddressSelectFormView, self).form_valid(*args, **kwargs)
		print form
		return form

	def get_success_url(self, *args, **kwargs):
		return "/checkout/"