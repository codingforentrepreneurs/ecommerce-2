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

	def form_valid(self, form, *args, **kwargs):
		billing_address = form.cleaned_data["billing_address"]
		shipping_address = form.cleaned_data["shipping_address"]
		self.request.session["billing_address_id"] = billing_address.id
		self.request.session["shipping_address_id"] = shipping_address.id
		return  super(AddressSelectFormView, self).form_valid(form, *args, **kwargs)

	def get_success_url(self, *args, **kwargs):
		return "/checkout/"