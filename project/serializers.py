from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'age', 'gender', 'department', 'salary']

    def validate_age(self, value):
        if value > 60:
            raise serializers.ValidationError("Employee age cannot be more than 60.")
        return value

    def validate_gender(self, value):
        valid_genders = ['M', 'F', 'T']
        if value not in valid_genders:
            raise serializers.ValidationError("Gender should be M, F or T.")
        return value
