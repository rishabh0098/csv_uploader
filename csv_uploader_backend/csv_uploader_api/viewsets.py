from rest_framework import viewsets
from csv_uploader_api.models import Student
from csv_uploader_api.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()