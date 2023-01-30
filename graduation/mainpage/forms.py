from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}), label=_(u'Имя'))
    subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}), label=_(u'Тема'))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label=_(u'Отправитель'))
    message = forms.CharField(widget=forms.Textarea(attrs={ 'placeholder': 'message'}), )

    class Meta:
        model = User
        fields = ('name','subject','sender','message')
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}), label=_(u'Старый пароль'))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}), label=_(u'Новый пароль'))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}), label=_(u'Новый пароль'))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2',)

