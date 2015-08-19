from django import forms

from django.forms.models import modelformset_factory


from .models import Variation



class VariationInventoryForm(forms.ModelForm):
	class Meta:
		model = Variation
		fields = [
			"price",
			"sale_price",
			"inventory",
			"active",
		]


VariationInventoryFormSet = modelformset_factory(Variation, form=VariationInventoryForm, extra=0)