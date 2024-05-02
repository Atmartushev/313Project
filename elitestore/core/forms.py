from django import forms
from .models import ProductVariation

from django import forms
from .models import ProductVariation

class AddToCartForm(forms.Form):
    color = forms.CharField(label='Color', max_length=50, widget=forms.Select)
    size = forms.CharField(label='Size', max_length=50, widget=forms.Select)

    def __init__(self, *args, **kwargs):
        product_variations = kwargs.pop('product_variations', None)
        super(AddToCartForm, self).__init__(*args, **kwargs)
        
        if product_variations:
            variations_with_both = product_variations.exclude(color__isnull=True).exclude(size__isnull=True)
            colors = variations_with_both.values_list('color', flat=True).distinct()
            self.fields['color'].widget.choices = [(color, color) for color in colors]

            # Check if color is selected and filter sizes accordingly
            if 'data' in kwargs:
                selected_color = kwargs['data'].get('color')
                if selected_color:
                    sizes = variations_with_both.filter(color=selected_color).values_list('size', flat=True).distinct()
                    self.fields['size'].widget.choices = [(size, size) for size in sizes]

