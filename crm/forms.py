from django import forms
from django.forms import ModelForm
from .models import *




class Leadsform(ModelForm):
    sur_name = forms.CharField(label='Familiya',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Ismingiz',widget=forms.TextInput(attrs={'class':'form-control'}))
    numbers = forms.CharField(label='Tel.raqam',widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label='Manzil',widget=forms.TextInput(attrs={'class':'form-control'}))
    service = forms.SelectMultiple()
    employees = forms.SelectMultiple()
    search_traffic = forms.SelectMultiple()
    sales_funnel = forms.SelectMultiple()
    class Meta:
        model = Lead
        fields = ('sur_name', 'last_name', 'numbers', 'address','service', 'employees', 'search_traffic', 'sales_funnel','address',)

class Projectform(ModelForm):
    name = forms.CharField()
    name_lead = forms.SelectMultiple()
    address = forms.CharField()
    numbers = forms.IntegerField()
    department = forms.SelectMultiple()
    data_end = forms.DateTimeField(widget=forms.DateInput())
    status_pay = forms.SelectMultiple()
    # pay = forms.SelectMultiple()
    # files = forms.FileField()
    class Meta:
        model = Project
        fields = ('name','name_lead','address','numbers','department','data_end','status_pay',)


class UpdateLead(ModelForm):
    service = forms.SelectMultiple()
    employees = forms.SelectMultiple()
    sales_funnel = forms.SelectMultiple()
    address = forms.CharField()

    class Meta:
        model = Lead
        fields = ['service', 'employees', 'sales_funnel', 'address']
