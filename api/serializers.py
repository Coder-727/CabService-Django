from rest_framework import serializers
from .models import  Ride,User, Cab, location


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'password', 'name', 'phone', 'gender', 
            'employeeid', 'designation', 'is_driver', 'car_model', 'license_plate'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    def validate(self, data):
        if data.get('is_driver'):
            if not data.get('car_model'):
                raise serializers.ValidationError({"car_model": "This field is required for drivers."})
            if not data.get('license_plate'):
                raise serializers.ValidationError({"license_plate": "This field is required for drivers."})
        return data

class CabSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_driver=True))

    class Meta:
        model = Cab
        fields = ['id','driver', 'start', 'destination', 'availableSeats', 'startTime', 'date']

    def create(self, validated_data):
        return Cab.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.start = validated_data.get('start', instance.start)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.availableSeats = validated_data.get('availableSeats', instance.availableSeats)
        instance.startTime = validated_data.get('startTime', instance.startTime)
        instance.date = validated_data.get('date', instance.date)
        instance.driver = validated_data.get('driver', instance.driver)
        instance.save()
        return instance
    
class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = location
        fields = '__all__'