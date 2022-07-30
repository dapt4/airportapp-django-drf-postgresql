from django.contrib.auth.models import User
from .models import Seat, Airplane, Ticket
from rest_framework import serializers

class SeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seat
        fields= ['id','number', 'first_class']

class AirplaneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Airplane
        fields = ['id','model', 'name']

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    seat = serializers.SlugRelatedField(
        read_only=True,
        slug_field='number'
    )
    airplane = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Ticket
        fields = ['id', 'date', 'hour', 'origin', 'destination', 'seat', 'airplane']
