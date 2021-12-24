from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.PersonListView.as_view(), name='person_changelist'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    path('ajax/load-district/', views.load_district, name='ajax_load_district'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
