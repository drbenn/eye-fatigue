from django.shortcuts import render

from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

# Create your views here.
class ItemListView(APIView):
    def get(self, request: Any) -> Response:
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request: Any) -> Response:
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class RustProcessView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Call Rust executable and capture output
            result = subprocess.run(["./rust_program"], capture_output=True, text=True)
            return Response(result.stdout.strip(), status=200)
        except Exception as e:
            return Response(str(e), status=500)

class TensorFlowProcessView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Call external Python TensorFlow script
            result = subprocess.run(["python", "tensorflow_module.py"], capture_output=True, text=True)
            return Response(result.stdout.strip(), status=200)
        except Exception as e:
            return Response(str(e), status=500)