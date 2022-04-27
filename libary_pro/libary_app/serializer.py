from rest_framework import serializers
from .models import *

class Admin_serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_Details
        fields = '__all__'

class Book_serializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Details
        fields = '__all__'        