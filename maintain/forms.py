"""
Forms
"""
from django import forms, utils


class MileageForm(forms.Form):
    mileage = forms.FloatField(required=True)
    fuel = forms.FloatField(required=False)
    date = forms.DateField(required=True, localize=True, initial=utils.timezone.now)


class ServiceForm(forms.Form):
    prefix = "service"

    date = forms.DateField(
        required=True,
        localize=True,
        initial=utils.timezone.now,
        label="Date of Service",
    )
    mileage = forms.FloatField(required=True, label="Current Vehicle Mileage")
    name = forms.CharField(required=True, label="Service")


class PartForm(forms.Form):
    """
    Class for adding parts to a Service.
    """

    name = forms.CharField(required=True, label="Part Name")
    number = forms.CharField(required=False, label="Part Number")


PartFormSet = forms.formset_factory(PartForm)


class ReminderForm(forms.Form):
    prefix = "reminder"

    duration = forms.FloatField(required=False, label="Time from service (in months)")
    miles = forms.FloatField(required=False, label="Miles from service")
