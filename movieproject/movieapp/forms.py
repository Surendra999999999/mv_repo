from django import forms
from movieapp.models import Movie
class MovieForm(forms.ModelForm):
    rdate = forms.DateField()
    movie_name = forms.CharField()
    hero = forms.CharField()
    heroine = forms.CharField()
    rating = forms.FloatField()
    class Meta:
        model = Movie
        fields = '__all__'
