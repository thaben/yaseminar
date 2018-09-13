from django.contrib.auth.models import User
import django_filters

from seminar.models import Seminar

class SeminarFilter(django_filters.FilterSet):
	
	title = django_filters.CharFilter(lookup_expr='icontains')
	location = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Seminar
		fields = ['title', 'category', 'location' ]



	def __init__(self, *args, **kwargs):
		super(SeminarFilter, self).__init__(*args, **kwargs)
		# at startup user doen't push Submit button, and QueryDict (in data) is empty
		if self.data == {}:
			self.queryset = self.queryset.none()
