from django import forms
from django.forms import inlineformset_factory
from .models import OpsBriefMinutes, Minutes

OBMinutesFormSet = inlineformset_factory(OpsBriefMinutes, Minutes, fields=('who_talked', 'write_up',))
