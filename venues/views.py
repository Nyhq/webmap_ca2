from rest_framework import viewsets
from .models import Venue, Review
from .serializers import VenueSerializer, ReviewSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

    def retrieve(self, request, pk=None):
        venue = get_object_or_404(self.queryset, pk=pk)
        reviews = Review.objects.filter(venue=venue)
        venue_serializer = self.serializer_class(venue)
        reviews_serializer = ReviewSerializer(reviews, many=True)
        data = {
            'venue': venue_serializer.data,
            'reviews': reviews_serializer.data,
        }
        return Response(data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    else:
        return Response({"error": "Invalid Credentials"}, status=400)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Ensure that TokenAuthentication is used
@permission_classes([IsAuthenticated])  # Ensure that only authenticated users can submit reviews
def submit_review(request):
    data = request.data
    data['user'] = request.user.id  # Attach the user to the review

    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
