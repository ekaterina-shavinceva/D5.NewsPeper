from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )



class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        authors_grupp = Group.objects.get(name='authors')
        user.groups.add(authors_grupp)

        send_mail(
            subject='Добро пожаловать на новостной сайт!',
            message=f'{user.username}, вы успешно зарегистрировались на нашем новостном порале!',
            from_email=None,
            recipient_list=[user.email],
        )
        return user
