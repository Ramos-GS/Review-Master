from django import forms
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]

    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select)
    comment = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 200}))

    class Meta:
        model = Review
        fields = ['rating', 'comment']
