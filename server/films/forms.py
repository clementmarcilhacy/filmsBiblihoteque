from django import forms

from .models import Film

class FilmForm(forms.ModelForm):
    title   = forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control col-lg-6", "placeholder": "Your title"}))
    year    = forms.IntegerField(initial=2005, widget=forms.NumberInput(attrs={"class":"form-control col-lg-6"}))
    imgUrl  = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control col-lg-6"}))

    class Meta:
        model = Film
        fields = [
            'title',
            'year',
            'imgUrl'
        ]

class RawFilmForm(forms.Form):
    title   = forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control col-lg-6", "placeholder": "Your title"}))
    year    = forms.IntegerField(initial=2005, widget=forms.NumberInput(attrs={"class":"form-control col-lg-6"}))
    imgUrl  = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control col-lg-6"}))
