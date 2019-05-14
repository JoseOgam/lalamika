from django import forms
from . import models
from .models import Viewtranscript, Complaints


class UserTranscriptForm(forms.ModelForm):
    my_sem = forms.ModelChoiceField(queryset=models.Semester.objects.values_list('sem', flat=True),
                                    to_field_name='id', empty_label='select semester')

    class Meta:
        model = Viewtranscript
        fields = ['my_sem', ]


class UserComplaintsForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
    description = forms.CharField(help_text='create your complaint here', widget=forms.Textarea)

    class Meta:
        model = Complaints
        fields = ['title', 'description']
