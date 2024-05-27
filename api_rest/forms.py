from django import forms
from django.forms import ValidationError
from .models import User


class UserForm(forms.ModelForm):
    nickname = forms.CharField(
        label='Usuário',
    )
    name = forms.CharField(
        label='Nome completo',
    )
    email = forms.EmailField(
        label='E-mail',
    )
    age = forms.IntegerField(
        label='Idade',
    )

    class Meta:
        model = User
        fields = ['nickname', 'name', 'email', 'age']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        'E-mail já existe. Digite outro.', code='invalid')
                )
        return email

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        current_nickname = self.instance.nickname

        if current_nickname != nickname:
            if User.objects.filter(nickname=nickname).exists():
                self.add_error(
                    'nickname',
                    ValidationError(
                        'Nickname já existe. Digite outro.', code='invalid')
                )
        return nickname
