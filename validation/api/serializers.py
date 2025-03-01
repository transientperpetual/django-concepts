from rest_framework import serializers
from .models import Student

#Validator

def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with R')

#base class is enough to read data from model
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[starts_with_r])
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
    
    # Field Level Validation
    # here value is the the value of the field that is being validated.
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    #Object Level Validation
    #here data is the data that is coming from client, here it is a dictionary.
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'sachin' and ct.lower() != 'mumbai':
            raise serializers.ValidationError('City must be Mumbai')
        return data
            
