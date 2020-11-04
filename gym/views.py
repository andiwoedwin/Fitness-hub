from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import ProgrammeSerializer
from .models import Programme


class ProgrammeList(APIView):

    def get(self, request):
        Programme1 = Programme.objects.all()
        serializer=ProgrammeSerializer(Programme1, many=True)
        return Response(serializer.data)

    # def_post(self):

