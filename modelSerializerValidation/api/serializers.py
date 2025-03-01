from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    # Custom Validation
    def starts_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with R')
    name = serializers.CharField(validators=[starts_with_r])
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {'name': {'read_only': True}, 'roll': {'read_only': True}}

        # Field Level Validation
    # here value is the the value of the field that is being validated.
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    #Object Level Validation
    #here data is the data that is coming from client, here it is a dictionary.
    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'sachin' and ct.lower() != 'mumbai':
    #         raise serializers.ValidationError('City must be Mumbai')
    #     return data
    
 
