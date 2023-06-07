from django import forms


REALTY_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 7)]


class CartAddRealtyForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=REALTY_QUANTITY_CHOICES,
                                coerce=int,
                                label="Кол-во дней: ")
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
