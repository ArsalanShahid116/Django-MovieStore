from django import forms
from django.contrib.auth import get_user_model

from moviesApp.models import Vote, myMovie

class VoteForm(forms.ModelForm):

    user = forms.ModelChoiceField(
            widget=forms.HiddenInput,
            queryset=get_user_model().
            objects.all(),
            disabled=True,
            )
    movie = forms.ModelChoiceField(
            widget=forms.HiddenInput,
            queryset=myMovie.objects.all(),
            disabled=True
            )
    value = forms.ChoiceField(
            label='Vote',
            widget=forms.RadioSelect,
            choices=Vote.VALUE_CHOICES,
            )

    class Meta:
        model = Vote
        fields = (
            'value', 'user', 'movie',)

