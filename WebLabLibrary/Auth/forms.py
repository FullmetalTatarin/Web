from django import forms


class RegForm(forms.Form):
    name = forms.CharField(max_length=25, label="Имя", required=True,
                           widget=forms.TextInput(attrs={'class': 'name'}))
    login = forms.CharField(max_length=25, label="Логин", required=True,
                            widget=forms.TextInput(attrs={'class': 'login'}))
    password = forms.CharField(max_length=25, label="Пароль", required=True,
                               widget=forms.PasswordInput(attrs={'class': 'password'}))
    rep_password = forms.CharField(max_length=25, label="Повторите пароль",
                                   required=True, widget=forms.PasswordInput(attrs={'class': 'rep-password'}))
    email = forms.CharField(max_length=25, label="E-mail",
                            required=True, widget=forms.TextInput(attrs={'class': 'email'}))


class LoginForm(forms.Form):
    login = forms.CharField(max_length=25, label="Логин", required=True,
                            widget=forms.TextInput(attrs={'class': 'login'}))
    password = forms.CharField(max_length=25, label="Пароль", required=True,
                               widget=forms.PasswordInput(attrs={'class': 'password'}))
