from django import forms
from django.core.validators import MaxValueValidator


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=30)
    num = forms.IntegerField(max_value=50, min_value=1)

    # class Meta:
    #     model = VideoInfo
    #     fields = ["keyword"]
