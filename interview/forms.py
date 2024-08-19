from django import forms
from .models import Interview,Hr


class InterviewForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Interview
        fields = '__all__'
    # result = forms.CharField(required=False)  # This explicitly makes the field optional


class HrForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Hr
        fields = '__all__'