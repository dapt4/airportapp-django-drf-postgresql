from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from .models import Seat, Airplane, Ticket
from .serializers import SeatSerializer, AirplaneSerializer, TicketSerializer

# Create your views here.
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny,])
def sigin(request):
    try:
        user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        )
        if not user:
            return Response({'error':'invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({'error':'internal server error'})

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny,])
def signup(request):
    try:
        user = User(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        return Response({'message':'register done'})
    except Exception as err:
        print(err)
        return Response({'error':'internal server error'})

@csrf_exempt
@api_view(['POST','GET'])
def seat(request):
    try:
        if request.method == 'GET':
            seats = Seat.objects.all()
            serializer = SeatSerializer(seats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = SeatSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({'error':'internal server error'})

@csrf_exempt
@api_view(['POST', 'GET'])
def airplane(request):
    try:
        if request.method == 'GET':
            airplanes = Airplane.objects.all()
            serializer = AirplaneSerializer(airplanes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'POST':
            serializer = AirplaneSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)
        return Response({'error':'internal server error'})

@csrf_exempt
@api_view(['POST','GET'])
def ticket(request):
    try:
        user = request.user
        if request.method == 'GET':
            tickets = user.tickets.all()
            serializer = TicketSerializer(tickets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'POST':
            seat = Seat.objects.get(id=request.data['seat'])
            airplane = Airplane.objects.get(id=request.data['airplane'])
            ticket = Ticket(
                date = request.data['date'],
                hour = request.data['hour'],
                origin = request.data['origin'],
                destination = request.data['destination'],
                seat = seat,
                airplane = airplane,
                user=user
            )
            ticket.save()
            serializer = TicketSerializer(ticket)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error":"invalid data"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response({'error':'internal server error'})

@csrf_exempt
@api_view(['GET', 'DELETE', 'PUT'])
def edit_ticket(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
        if request.method == 'GET':
            serializer = TicketSerializer(ticket)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            seat = Seat.objects.get(id=request.data['seat'])
            airplane = Airplane.objects.get(id=request.data['airplane'])
            ticket.date = request.data['date']
            ticket.hour = request.data['hour']
            ticket.origin = request.data['origin']
            ticket.destination = request.data['destination']
            ticket.seat = seat
            ticket.airplane = airplane
            ticket.save()
            serializer = TicketSerializer(ticket)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        if request.method == 'DELETE':
            ticket.delete()
            serializer = TicketSerializer(ticket)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({'error':'internal server error'})
