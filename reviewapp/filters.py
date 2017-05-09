from .models import Therapist
import django_filters

class TherapistFilter(django_filters.FilterSet):
    class Meta:
        model = Therapist
        fields = ['name', 'last_name', 'tags', ]
