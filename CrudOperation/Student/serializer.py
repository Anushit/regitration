from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def create(self, validated_data):
        validated_data['Firstname'] = self.validated_data.get('Firstname')
        validated_data['lastname'] = self.validated_data.get('lastname')
        validated_data['email'] = self.validated_data.get('email')
        return super(EmployeeSerializer, self).create(validated_data)