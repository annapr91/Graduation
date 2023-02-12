import re

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm

from django import forms
from django.core.exceptions import ValidationError

from .models import Child, Kindergarden, User


class RegisUserForm(UserCreationForm):

    first_name = forms.CharField(label=('Имя'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label=('Фамилия'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label=('Почта'),
                             widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Почта'}))
    username = forms.CharField(label=('Логин'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label=('Пароль'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label=('Повтор пароля'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))



    class Meta:
        model = User
        fields = ('first_name','last_name','username','email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == self.cleaned_data['last_name'] :
            raise ValidationError('Usernane cant be the same as last_name')
        elif username == self.cleaned_data['first_name']:
            raise ValidationError('Usernane cant be the same as first_name')

        return username
class RegistrationKind(forms.ModelForm):
    error_messages = {
        "password_mismatch": ("The name type should be str not int."),
        "surname_mismatch": ("The surname type should be str not int."),
        "id_number_mismatch":("Длинна Ид-номера должна состоять из 8 символов.Пожалуйста,проверьте")
    }
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input','placeholder': 'Имя'}))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    det_sads = forms.ModelChoiceField(queryset= Kindergarden.objects.all(),label='Детский сад')
    id_number = forms.CharField(label='Ид', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Child
        fields = ['name', 'surname', 'det_sads','id_number']

    def clean_name(self):
        number = [0,1,2,3,4,5,6,7,8,9]
        name= self.cleaned_data.get('name')

        for el in number:
            if str(el) in name:
                raise ValidationError(
                    self.error_messages["password_mismatch"],
                    code="password_mismatch",
                )
        return name

    def clean_surname(self):
        number = [0,1,2,3,4,5,6,7,8,9]
        surname= self.cleaned_data.get('surname')

        for el in number:
            if str(el) in surname:
                print(el)
                print(self.cleaned_data.get('surname'))
                raise ValidationError(
                    self.error_messages["surname_mismatch"],
                    code="surname_mismatch",
                )

        return surname

    def clean_id_number(self):
        id_number=self.cleaned_data.get('id_number')
        if len(id_number)!=8:
            raise ValidationError(
                self.error_messages['id_number_mismatch']
            )
        return id_number
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # password1 = forms.CharField(label='Пароль1', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = ['username', 'password1']

class PasswordReset(PasswordResetForm):
    email=forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input','placeholder': 'Почта'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UserNameChange(forms.ModelForm):
    error_messages = {
        'address_mismatch': ('Пожалуйста,проверьте адрес  - улица,дом/кварира.'),
        'phone_mismatch': (' Пожалуйста,проверьте номер телефона (8 цифр).')
    }
    username = forms.CharField(label='Ваше имя', max_length=255)
    first_name = forms.CharField(label='Фамилия', max_length=255)
    last_name = forms.CharField(label='Фамилия', max_length=255)
    email = forms.EmailField(label='Ваша почта', max_length=255,widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': ('почта')})),
    phone = forms.IntegerField(localize=False, label=('Телефон'),
                               widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': ('телефон')}))
    address = forms.CharField(label=('Адрес'), widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': ('улица,дом/квартира')}))


    def clean_address(self):
        data = self.cleaned_data['address']
        c = re.match(r'^[а-яА-яa-zA-Z]+,\d+/\d+$', data)
        print(c)
        if not c:
            raise ValidationError(
                         self.error_messages['address_mismatch'],
                         code='address_mismatch',
                     )
        return data

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(str(phone))!=8:
            raise ValidationError(
                self.error_messages['phone_mismatch'],
                code='phone_mismatch',
            )

        return phone

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == self.cleaned_data['last_name'] :
            raise ValidationError('Usernane cant be the same as last_name')
        elif username == self.cleaned_data['first_name']:
            raise ValidationError('Usernane cant be the same as first_name')

        return username

    class Meta:
        model = User
        fields = ['last_name','first_name','username', 'email', 'phone', 'address']




