from rest_framework import routers, serializers
from .models import Student,Customer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'