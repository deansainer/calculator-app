from django import forms


class HomeForm(forms.Form):
    num1 = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter first num:'}))
    num2 = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter second num:'}))
