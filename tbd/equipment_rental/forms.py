from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Equipment
from .models import Client

class EquipmentForm(forms.ModelForm):
    class Meta:
        model= Equipment
        exclude = ['stock_available']

    def __init__(self,*args,**kwargs):
        super(EquipmentForm,self).__init__(*args,**kwargs)
        self.helper= FormHelper()
        self.helper.wrapper_class = 'row'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit','Guardar',css_class='btn-primary'))

class ClientForm(forms.ModelForm):
    class Meta:
        model= Client
        exclude = []

    def __init__(self,*args,**kwargs):
        super(ClientForm,self).__init__(*args,**kwargs)
        self.helper= FormHelper()
        self.helper.wrapper_class = 'row'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.add_input(Submit('submit','Guardar',css_class='btn-primary'))
