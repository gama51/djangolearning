from django import forms
from django.forms.formsets import MAX_NUM_FORM_COUNT

class ProfileForm(forms.Form):
    website=forms.URLField(max_length=200,required=True)
    biography=forms.CharField(max_length=500,required=False)
    phone_number=forms.CharField(max_length=20, required=False)
    picture=forms.ImageField()
