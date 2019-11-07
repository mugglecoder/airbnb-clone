from django import forms
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(initial="anywhere")
    price = forms.IntegerField(required=False)
    room_types = forms.ModelChoiceField(queryset=models.RoomType.objects.all())
