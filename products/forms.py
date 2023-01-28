# -*- coding: utf-8 -*-
from django import forms

from .models import Iteams

    
        

class IteamsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IteamsForm, self).__init__(*args, **kwargs)
        self.fields['iteam_code'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['iteam_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['iteam_mes_para'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['iteam_qty'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['supplier_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['employee_name'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = Iteams
        fields = ('iteam_code', 'iteam_name', 'iteam_mes_para','iteam_qty','image','supplier_name','employee_name')