from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Participante, Tutor_IA, Tutor, Curso, Documento
from .serializer import ParticipanteSerializer, Tutor_IASerializer, TutorSerializer, CursoSerializer, DocumentoSerializer
from rest_framework import viewsets
from django.core.files.base import ContentFile
from django.conf import settings



class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

class TutorIAViewSet(viewsets.ModelViewSet):
    queryset = Tutor_IA.objects.all()
    serializer_class = Tutor_IASerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

def create(self, request, *args, **kwargs):
        file_content = request.data.get('documento', None)

        if file_content is not None:
            # Save the file content in the database
            documento_instance = Documento.objects.create(
                nombre=request.data.get('nombre'),
                tipo=request.data.get('tipo'),
                formato=request.data.get('formato'),
                archivo=file_content
            )
            serializer = self.get_serializer(documento_instance)
            return Response(serializer.data, status=201)
        else:
            # If no file content is received, save a default empty file
            default_content = b''  # Replace this with your desired default content
            default_file = ContentFile(default_content, name='default_file.txt')

            documento_instance = Documento.objects.create(
                nombre=request.data.get('nombre'),
                tipo=request.data.get('tipo'),
                formato=request.data.get('formato'),
                archivo=default_file
            )
            serializer = self.get_serializer(documento_instance)
            return Response(serializer.data, status=201)