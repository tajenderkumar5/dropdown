from django import forms
from .models import  City, District, Person, States

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name','birthdate','country','states','district','city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['states'].queryset = States.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['states'].queryset = States.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['states'].queryset = self.instance.country.states_set.order_by('name')

        self.fields['district'].queryset = States.objects.none()
         
        if 'states' in self.data:
            try:
                states_id = int(self.data.get('states'))
                self.fields['district'].queryset = District.objects.filter(states_id=states_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.states.district_set.order_by('name')     
        
        
        # self.fields['city'].queryset = States.objects.none()
        # if 'district' in self.data:
        #     try:
        #         city_id = int(self.data.get('city'))
        #         self.fields['city'].queryset = City.objects.filter(city_id=city_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['city'].queryset = self.instance.district.city_set.order_by('name') 
     
