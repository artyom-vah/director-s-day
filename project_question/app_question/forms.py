from django import forms
from .models import *
from smart_selects.form_fields import ChainedModelChoiceField


class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['name', ]
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'})
        }


class EnterpriseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['division'].empty_label = 'Выберите ваш дивизион'

    class Meta:
        model = Enterprise
        fields = ['name', 'division']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'division': forms.Select(attrs={'class': 'form-control'})
        }


class AddQuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['enterprise'].required = False
        self.fields['enterprise'].empty_label = 'другое'

    class Meta:
        model = Question
        fields = ['enterprise', 'email', 'question']
        widgets = {
            'enterprise': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'question': forms.Textarea(attrs={'class': 'form-control'}),
        }

