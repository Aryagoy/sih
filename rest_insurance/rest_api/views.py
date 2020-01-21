
from .serializers import vitalSerializer, vitalSerializer2,vitalSerializer3,chronicSerializer1,chronicSerializer3,chronicSerializer2
from rest_framework import generics

from insurance.models import vital,vital2,vital3,chronic_month3,chronic_month2,chronic

class trendchart(generics.ListAPIView):
	lookup_field = 'id'
	queryset = vital.objects.all()
	serializer_class = vitalSerializer

class trendchart1(generics.ListAPIView):
	lookup_field = 'id'
	queryset = vital2.objects.all()
	serializer_class = vitalSerializer2

class trendchart2(generics.ListAPIView):
	lookup_field = 'id'
	queryset = vital3.objects.all()
	serializer_class = vitalSerializer3

class trendchart3(generics.ListAPIView):
	lookup_field = 'id'
	queryset = chronic.objects.all()
	serializer_class = chronicSerializer1
class trendchart4(generics.ListAPIView):
	lookup_field = 'id'
	queryset = chronic_month2.objects.all()
	serializer_class = chronicSerializer2
class trendchart5(generics.ListAPIView):
	lookup_field = 'id'
	queryset = chronic_month3.objects.all()
	serializer_class = chronicSerializer3		
