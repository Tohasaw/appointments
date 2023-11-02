from .models import *
from django import forms
from django.db.models import Max

class AppsCustomerNewForm(forms.Form):
  service = forms.ModelChoiceField(
    label = 'Услуга',
    queryset=PriceListPosition.objects.all(),
    widget=forms.Select(
      attrs={
        'id': 'id_service',
        'autocomplete': 'off'
      }
    )
  )
  employee = forms.ModelChoiceField(
    label = 'Мастер',
    queryset=Employee.objects.all(),
    widget=forms.Select(
      attrs={
        'id': 'id_employee',
        'autocomplete': 'off'
      }
    )
  )
  date = forms.DateField(
    label = 'Дата приема',
    widget=forms.DateInput(
      attrs={
        'id': 'id_date',
        'class': 'datepicker',
        'autocomplete': 'off',
        'readonly': 'readonly'
      },
    )
  )
  time = forms.MultipleChoiceField(
    label = 'Время приёма',
    widget= forms.Select(
      attrs={
        'id': 'time_slot_container',
        'autocomplete': 'off',
        'readonly': 'readonly'
      }
    ),
    choices=[('', 'Выберите время')]
  )

# EMPLOYEE FORMS

