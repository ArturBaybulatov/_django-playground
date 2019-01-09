from django import forms
import datetime


class TestForm(forms.Form):
    GENDERS = (
        ('', ''),
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    COUNTRIES = (
        ('', ''),
        ('australia', 'Australia'),
        ('china', 'China'),
        ('france', 'France'),
        ('germany', 'Germany'),
        ('india', 'India'),
        ('italy', 'Italy'),
        ('japan', 'Japan'),
        ('russia', 'Russia'),
        ('spain', 'Spain'),
        ('united-states', 'United States'),
    )

    error_css_class = 'field--errored'
    required_css_class = 'field--required'

    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    gender = forms.ChoiceField(choices=GENDERS)
    birth_date = forms.DateField(required=False)
    country = forms.ChoiceField(choices=COUNTRIES, required=False)
    married = forms.BooleanField(required=False)
    years_married = forms.IntegerField(required=False)
    salary = forms.DecimalField(required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('gender') == 'female' and cleaned_data.get('birth_date') >= datetime.date(2000, 1, 1):
            raise forms.ValidationError('No females born past 2000-01-01')

        if cleaned_data.get('married'):
            raise forms.ValidationError({'years_married': 'Validation for "years married"'})

        return cleaned_data


# import code; code.interact(local=dict(globals(), **locals()))
