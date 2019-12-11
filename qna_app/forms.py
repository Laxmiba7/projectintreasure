from django import forms
from .models import QuestionModel,AnswerModel

class QuestionForm(forms.ModelForm):
    class Meta:             #change attribute of parent form
        model= QuestionForm
        fields='__all__'
