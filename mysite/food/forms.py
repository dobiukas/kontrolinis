from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm


class food(ModelForm):
    class Meta:
        model = Food
        fields = "__all__"


class UserFood(ModelForm):
    class Meta:
        model = UserFood
        fields = "__all__"


class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']