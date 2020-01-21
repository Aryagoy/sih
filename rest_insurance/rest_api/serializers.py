from rest_framework import serializers

from insurance.models import vital,vital2,vital3,chronic,chronic_month2,chronic_month3

class vitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = vital
        fields ="__all__"
        #read_only_fields = ['pk','title']

class vitalSerializer2(serializers.ModelSerializer):
    class Meta:
        model = vital2
        fields ="__all__"
        #read_only_fields = ['pk','title']

class vitalSerializer3(serializers.ModelSerializer):
    class Meta:
        model = vital3
        fields ="__all__"
        #read_only_fields = ['pk','title']

class chronicSerializer1(serializers.ModelSerializer):
    class Meta:
        model = chronic
        fields ="__all__"
        #read_only_fields = ['pk','title']
class chronicSerializer2(serializers.ModelSerializer):
    class Meta:
        model = chronic_month2
        fields ="__all__"
        #read_only_fields = ['pk','title']

class chronicSerializer3(serializers.ModelSerializer):
    class Meta:
        model = chronic_month3
        fields ="__all__"
        #read_only_fields = ['pk','title']
