from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Musician
from .serializers import MusicianSerializer
# Alternative: Function-based views for basic CRUD
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.exceptions import ValidationError
import json


class MusicianListCreateView(generics.ListCreateAPIView):
    """GET: List all musicians, POST: Create a new musician"""

    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianDetailView(generics.RetrieveUpdateDestroyAPIView):
    """GET: Retrieve a musician, PUT/PATCH: Update, DELETE: Remove"""

    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


@csrf_exempt
def musician_list(request):
    """GET all musicians or POST create new musician"""
    if request.method == "GET":
        musicians = Musician.objects.all()
        data = []
        for musician in musicians:
            data.append(
                {
                    "id": musician.id,
                    "first_name": musician.first_name,
                    "last_name": musician.last_name,
                    "instrument": musician.instrument,
                    "age": musician.age,
                    "date_of_applying": musician.date_of_applying,
                    "is_adult": musician.is_adult,
                }
            )
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        try:
            musician = Musician.objects.create(
                first_name=data["first_name"],
                last_name=data["last_name"],
                instrument=data["instrument"],
                age=data["age"],
            )
            return JsonResponse(
                {
                    "id": musician.id,
                    "first_name": musician.first_name,
                    "last_name": musician.last_name,
                    "instrument": musician.instrument,
                    "age": musician.age,
                    "date_of_applying": musician.date_of_applying,
                    "is_adult": musician.is_adult,
                },
                status=201,
            )
        except ValidationError as e:
            return JsonResponse({"error": e.message_dict}, status=400)
        except KeyError as e:
            return JsonResponse({"error": f"Missing field: {e}"}, status=400)


@csrf_exempt
def musician_detail(request, pk):
    """GET, PUT, DELETE specific musician by id"""
    try:
        musician = Musician.objects.get(pk=pk)
    except Musician.DoesNotExist:
        return JsonResponse({"error": "Musician not found"}, status=404)

    if request.method == "GET":
        data = {
            "id": musician.id,
            "first_name": musician.first_name,
            "last_name": musician.last_name,
            "instrument": musician.instrument,
            "age": musician.age,
            "date_of_applying": musician.date_of_applying,
            "is_adult": musician.is_adult,
        }
        return JsonResponse(data)

    elif request.method == "PUT":
        data = json.loads(request.body)
        try:
            musician.first_name = data.get("first_name", musician.first_name)
            musician.last_name = data.get("last_name", musician.last_name)
            musician.instrument = data.get("instrument", musician.instrument)
            musician.age = data.get("age", musician.age)
            musician.clean()  # Validate age
            musician.save()
            return JsonResponse(
                {
                    "id": musician.id,
                    "first_name": musician.first_name,
                    "last_name": musician.last_name,
                    "instrument": musician.instrument,
                    "age": musician.age,
                    "date_of_applying": musician.date_of_applying,
                    "is_adult": musician.is_adult,
                }
            )
        except ValidationError as e:
            return JsonResponse({"error": e.message_dict}, status=400)

    elif request.method == "DELETE":
        musician.delete()
        return JsonResponse(
            {"message": "Musician deleted successfully"}, status=204
        )
