from django import forms


class ChoiceForm(forms.Form):
    funk = forms.ChoiceField(
        choices=[('D', 'Кубик'), ('B', 'Монетка'), ('R', 'Случайное число до 100')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    repeats = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
