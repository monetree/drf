from rest_framework import serializers
from .models import Company,Language,Frameworks,Technologies

class GetLanguageSerializer(serializers.ModelSerializer):
    technology = serializers.StringRelatedField(many=True)
    frameworks = serializers.StringRelatedField(many=True)
    total_technology = serializers.SerializerMethodField(read_only=True)
    total_frameworks = serializers.SerializerMethodField(read_only=True)

    def get_total_frameworks(self, language):
        return language.frameworks.count()

    def get_total_technology(self, language):
        return language.technology.count()

    class Meta:
        model = Language
        fields = ('language_name','created_on','latest_build_on','latest_version','company','technology','total_technology','frameworks','total_frameworks')
        depth = 1


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('language_name','created_on','latest_build_on','latest_version','company')



class GetFrameworksSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()
    class Meta:
        model = Frameworks
        fields = '__all__'
        depth = 1

class FrameworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frameworks
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()
    class Meta:
        model = Company
        fields = ('company_name','started_from','country','email','website','ip','active','language')

class GetTechnologiesSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField(many=True)
    class Meta:
        model = Technologies
        fields = '__all__'

class TechnologiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Technologies
        fields = '__all__'
