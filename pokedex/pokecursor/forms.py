import django.forms as forms


class IntegerForm(forms.Form):
    num_times = forms.IntegerField(label='Ingrese un número entero(Se multiplica por 800 datos)', min_value=1, max_value=20)

class FilterForm(forms.Form):
    name_filter = forms.CharField(label='Nombre', max_length=20)