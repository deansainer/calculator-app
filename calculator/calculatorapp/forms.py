from django import forms


class HomeForm(forms.Form):
    number1 = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter first num:', 'class': 'form-control'}))
    number2 = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter second num:', 'class': 'form-control'}))
