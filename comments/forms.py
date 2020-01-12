from django import forms
from .models import Question
from django.contrib.auth.models import User


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question', 'user',)
        exclude = ('user', )
