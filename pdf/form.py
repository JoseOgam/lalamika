from django import forms
from . import models
from .models import Viewtranscript, Complaints, Transcript


# class UserTranscriptForm(forms.ModelForm):
#   my_sem = forms.ModelChoiceField(queryset=
#                                  models.Semester.objects.all(),
#                                 to_field_name='id',
#                                empty_label='select semester')

# class Meta:
#   model = Viewtranscript
#  fields = ['my_sem', ]


class UserComplaintsForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
    description = forms.CharField(help_text='create your complaint here', widget=forms.Textarea)

    class Meta:
        model = Complaints
        fields = ['title', 'description']


class UserTranscriptForm(forms.ModelForm):
    regno = forms.CharField(max_length=30)
    unit_title = forms.CharField(max_length=100)
    unit_code = forms.IntegerField
    marks = forms.DecimalField(decimal_places=1, max_digits=13)

    class Meta:
        model = Transcript
        fields = ['semester', 'regno', 'marks']
