from django.http import JsonResponse, HttpResponse
from .models import Company,Language,Frameworks,Technologies
from .serializers import (
                            CompanySerializer,
                            LanguageSerializer,GetLanguageSerializer,
                            FrameworksSerializer,GetFrameworksSerializer,
                            TechnologiesSerializer,GetTechnologiesSerializer,
                        )
from rest_framework import viewsets
from rest_framework.filters import (
            SearchFilter,
            OrderingFilter
        )
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class CompanyView(viewsets.ModelViewSet):
    queryset =  Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['company_name','country','email','website','ip','active']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    def get_queryset(self):
        queryset = Company.objects.all()
        company_name = self.request.query_params.get('company_name', None)
        if company_name is not None:
            queryset = queryset.filter(company_name=company_name)
        return queryset

class LanguageView(viewsets.ModelViewSet):
    queryset =  Language.objects.all()
    serializer_class = LanguageSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['language_name']

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = GetLanguageSerializer
        return serializer_class

class FrameworksView(viewsets.ModelViewSet):
    queryset =  Frameworks.objects.all()
    serializer_class = FrameworksSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['framework_name']


    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = GetFrameworksSerializer
        return serializer_class

class TechnologiesView(viewsets.ModelViewSet):
    queryset =  Technologies.objects.all()
    serializer_class = TechnologiesSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['technology_name']

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = GetTechnologiesSerializer
        return serializer_class
