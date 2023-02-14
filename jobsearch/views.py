from django.shortcuts import render
from .models import Professional, JobAcademic, JobExperience
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import ProfessionalSerializer , JobExperienceSerializer, JobAcademicSerializer



class ProfessionalViewsSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self, request, id):
        user = self.request.user #pega usuario que esta logado
        return Professional.objects.filter(owner = user) 


class JobExperienceViewsSet(viewsets.ModelViewSet):
    
    serializer_class = JobExperienceSerializer


class JobAcademicViewsSet(viewsets.ModelViewSet):
    
    serializer_class = JobAcademicSerializer