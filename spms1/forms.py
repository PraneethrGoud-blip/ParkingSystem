from django import forms
from spms1.models import login
from .models import Vehicle, Category


class LoginForm(forms.ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Username'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )

    class Meta:
        model = login
        fields = "__all__"


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"

        widgets = {

            'parking_area_number':
            forms.NumberInput(attrs={
                'class':'form-control form-control-sm'
            }),

            'vehicle_type':
            forms.TextInput(attrs={
                'class':'form-control form-control-sm'
            }),

            'vehicle_limit':
            forms.NumberInput(attrs={
                'class':'form-control form-control-sm'
            }),

            'parking_charge':
            forms.NumberInput(attrs={
                'class':'form-control form-control-sm'
            }),
        }

class VehicleForm(forms.ModelForm):

    class Meta:

        model = Vehicle

        fields = [
            'vehicle_number',
            'vehicle_type',
            'area_number',
            'charges',
            'parking_status'
        ]

        widgets = {

            'vehicle_number':
            forms.TextInput(attrs={
                'class':'form-control'
            }),

            'vehicle_type':
            forms.Select(attrs={
                'class':'form-control'
            }),

            'area_number':
            forms.NumberInput(attrs={
                'class':'form-control'
            }),

            'charges':
            forms.NumberInput(attrs={
                'class':'form-control'
            }),

            'parking_status':
            forms.Select(attrs={
                'class':'form-control'
            }),
        }
