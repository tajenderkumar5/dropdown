from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import City, District, Person,Country, States
from .forms import PersonForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


def load_states(request):
    country_id = request.GET.get('country')
    states= States.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'db/states_dropdown_list.html', {'states': states})

def load_district(request):
    states_id = request.GET.get('states')
    district = District.objects.filter(states_id=states_id).order_by('name')
    return render(request, 'db/district_dropdown_list.html', {'district': district})

def load_cities(request):
    states_id = request.GET.get('states')
    cities = City.objects.filter(states_id=states_id).order_by('name')
    return render(request, 'db/city_dropdown_list_options.html', {'cities': cities})    