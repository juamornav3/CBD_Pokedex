import django.forms as forms
import pokecursor.cursor_helper as cursor_helper

class IntegerForm(forms.Form):
    num_times = forms.IntegerField(label='Ingrese un número entero(Se multiplica por 800 datos)', min_value=1, max_value=20)

class FilterForm(forms.Form):
    name_filter = forms.CharField(label='Nombre', max_length=20, required=False)
    type1_filter = forms.ChoiceField(choices=cursor_helper.get_type_with_cursor(), label='Tipo 1', widget=forms.Select, required=False)
    type2_filter = forms.ChoiceField(choices=cursor_helper.get_type_with_cursor(), label='Tipo 2', widget=forms.Select, required=False)
    gen_filter = forms.ChoiceField(choices=[("",""), ("1","1"), ("2","2"), ("3","3"), ("4","4"), ("5","5"), ("6","6"), ("7","7"), ("8","8")], label='Generación', widget=forms.Select, required=False)
    legendary_filter = forms.BooleanField(label='Legendario', required=False)