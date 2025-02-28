from rest_framework import serializers
from .models import Student

#base class is enough to read data from model
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    #to add data to model we need to create a create method
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    #to update data in model we need to create a update method
    #instance represents all data that is already present in model. validated_data represents the data that is coming from client
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
