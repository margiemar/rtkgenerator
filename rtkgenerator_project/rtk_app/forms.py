from django import forms
from django.core.exceptions import ValidationError
from .models import *

INCONTRACT_CHOICES = (('In contract', 'IN'), 
                      ('Not in contract', 'NEW'))

class OneTimeWorkForm(forms.ModelForm):
    #incontract =  forms.ChoiceField(widget=forms.RadioSelect, choices=INCONTRACT_CHOICES)

    class Meta:
        model = OneTimeWork
        fields = ['service_name', 'expert', 'hours', 'incontract']
        
        widgets = {
            'service_name': forms.Textarea(attrs={'cols': 130, 'rows': 1}),
            'expert': forms.Textarea(attrs={'cols': 160, 'rows': 1}),
            #'rate':
            'hours': forms.Textarea(attrs={'cols': 160, 'rows': 1}),   
            'incontract': forms.RadioSelect(choices=INCONTRACT_CHOICES)         
        }


class UserOrderForm(forms.ModelForm):

    #aso = forms.ModelChoiceField(queryset = ASOCatalog.objects.all(), label="ACO")
    aso = forms.ModelMultipleChoiceField(queryset = ASOCatalog.objects.all(),  widget=forms.CheckboxSelectMultiple, label="ACO")
    #one_time_operations = forms.ModelMultipleChoiceField

    class Meta:
        model = UserOrder
        fields = ['service_code', 'service_name', 'geo_address', 'aso', 'one_time_operations']
        widgets = {
            'service_code': forms.Textarea(attrs={'cols': 160, 'rows': 1}),
            'service_name': forms.Textarea(attrs={'cols': 160, 'rows': 1}),
            'geo_address': forms.Textarea(attrs={'cols': 160, 'rows': 1}), 
            'one_time_operations': forms.Textarea(attrs={'cols': 160, 'rows': 1}),

            #'aso': forms.ModelChoiceField(choices=ASOCatalog.objects.all()),
            #'one_time_operations': forms.ChoiceField(choices=OneTimeWork.objects.all())
        }

