from django.forms import ModelForm
from .models import Poll



class createPollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'option_1', 'option_2', 'option_3', 'option_4']