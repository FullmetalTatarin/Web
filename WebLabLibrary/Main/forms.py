from django import forms


class AddAndEditBookForm(forms.Form):
    name = forms.CharField(max_length=25, label="Название", required=True)
    author = forms.CharField(max_length=25, label="Автор", required=True)
    publisher = forms.CharField(max_length=25, label="Издатель", required=True)
    city = forms.CharField(max_length=25, label="Город издания", required=True)
    price = forms.FloatField(min_value=0, initial=0.0, required=True)
