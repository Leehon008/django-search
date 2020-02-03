# Create your views here.
from django.db.models import Q
from django.views.generic import TemplateView, ListView

from Cities.models import City, UserRegister


class Homepage(TemplateView):
    template_name = 'Cities/homepage.html'


class Login(TemplateView):
    template_name = 'Cities/login.html'


class Register(ListView):
    model = UserRegister
    template_name = 'Cities/register.html'


class CitySearches(ListView):
    model = City
    template_name = 'Cities/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
          Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list


class AllCities(ListView):
    model = City
    template_name = 'Cities/all_cities.html'

    def get_queryset(self):
        cities_object = City.objects.all()
        return cities_object

