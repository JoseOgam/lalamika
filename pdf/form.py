from django import forms
from . import models
from .models import Viewtranscript


class UserTranscriptForm(forms.ModelForm):
    my_sem = forms.ModelChoiceField(queryset=models.Semester.objects.values_list('sem', flat=True),
                                    to_field_name='id', empty_label='select semester')

    class Meta:
        model = Viewtranscript
        fields = ['my_sem', ]
