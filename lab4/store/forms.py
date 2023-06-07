from django import forms
from .models import Realty


class RealtyForm(forms.ModelForm):
    class Meta:
        model = Realty
        fields = ['name', 'owner', 'cost', 'type', 'description', 'image']
        labels = {
            'name': 'Название: ',
            'owner': 'Владелец: ',
            'cost': 'Стоимость за день: ',
            'type': 'Тип: ',
            'description': 'Описание: ',
            'image': 'Изображение: '
        }
