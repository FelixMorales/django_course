from django.forms import Form, BooleanField, CharField, ChoiceField, ModelChoiceField
from store.models import Category

ORDER_CHOICES = [
    ('PRICE_ASC', 'Price (lowest first)'),
    ('PRICE_DESC', 'Price (highest first)'),
    ('NAME', 'Name')
]

class FilterForm(Form):
    name = CharField(required=False)
    category = ModelChoiceField(queryset=Category.objects.all(), required=False)
    order_by = ChoiceField(choices=ORDER_CHOICES, required=False)
    only_in_stock = BooleanField(label="Only select products that are in stock.", required=False)