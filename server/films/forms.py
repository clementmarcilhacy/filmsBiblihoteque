from django import forms

from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = [
            'title',
            'year'
        ]

class RawFilmForm(forms.Form):
    title   = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control col-lg-6"}))
    year    = forms.IntegerField(initial=2005, widget=forms.NumberInput(attrs={"class":"form-control col-lg-6"}))
    imgUrl  = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control col-lg-6"}))
