from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length = 60,widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length = 60,widget = forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control'}))
    name_dog = forms.CharField(max_length = 60,widget = forms.TextInput(attrs={'class':'form-control'}))
    year_dog = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control'}))
    breed = forms.CharField(max_length = 60,widget = forms.TextInput(attrs={'class':'form-control'}))