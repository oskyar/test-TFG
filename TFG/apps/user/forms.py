__author__ = 'oskyar'

from django.contrib.auth.views import password_change
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm
from registration.models import RegistrationProfile
# from registration.models import UserModel
from TFG.apps.user.models import UserProfile
# Para traducir textos
from django.utils.translation import ugettext_lazy as _
import re
import datetime


class UserProfileForm(RegistrationForm):
    error_messages = dict(password_mismatch=_("Las dos contraseñas no coinciden."),
                          user_exists=_("El nombre de usuario no está disponible"),
                          email_exists=_("El correo electrónico ya existe, introduzca uno diferente"),
                          field_required=_("Es obligatorio rellenar el campo"),
                          emails_dont_match=_("Los correos electrónicos no coinciden"),
                          dni_format_invalid=_("El DNI no tiene el formato correcto, introduzca 8 letras y una letra"))

    username = forms.CharField(min_length=3, widget=forms.TextInput(attrs={'class': ''}), label=_("Nombre de usuario"))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), label=_("Nombre"))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), label=_("Apellidos"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'validate'}), label=_("Contraseña"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'validate'}),
                                label=_("Repita la contraseña"))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': ''}), label=_("Correo electrónico"))
    email2 = forms.EmailField(widget=forms.EmailInput(attrs={'class': ''}), label=_("Repita el correo electrónico"))
    dni = forms.CharField(min_length=9, max_length=9, required=False,
                          widget=forms.TextInput(attrs={'class': 'validate'}), label=_("DNI"))

    photo = forms.ImageField(required=False)
    created_on = forms.DateTimeField(required=False, initial=datetime.datetime.today())
    modify_on = forms.DateTimeField(required=False, initial=datetime.datetime.today())

    class Meta:
        model = User
        # fields = "__all__"
        fields = ["username", "first_name", "last_name", "email", "email2", "dni", "photo", "password1", "password2"]
        exclude = ["created_on", "modify_on"]

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            # self.widget_attrs({'class':'validate invalid'})
            raise forms.ValidationError(
                self.error_messages['user_exists'])

        # self.username.widget(setattr({'class':'validate valid'}))
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError(
                self.error_messages['email_exists'],

            )
        return email

    def clean_email2(self):
        email = self.cleaned_data['email']
        email2 = self.cleaned_data['email2']

        print(self.cleaned_data)
        if not email2:
            raise forms.ValidationError(self.error_messages['field_required'])
        if email and email2 and email != email2:
            raise forms.ValidationError(self.error_messages['emails_dont_match'])
        return email2

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if dni is not "":
            if not re.match("(\d{8}\w{1})", dni):
                raise forms.ValidationError(
                    self.error_messages['dni_format_invalid'],
                )
        return dni

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2