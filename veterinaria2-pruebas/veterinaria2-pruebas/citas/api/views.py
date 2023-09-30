from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from citas.api.serializers import *
from django.db import transaction
from citas.models import Cita, Servicio
import subprocess 

class CreateCita(APIView):
    @transaction.atomic
    def post(self,request):
        serializer = CitaCreateSerializer(data = request.data)
        fecha = request.data['fecha']
        bloque = request.data['id_bloque']
        servicio = request.data['id_servicio']
        # cupos en un bloque de horas
        cupo_bloque = Cita.objects.filter(fecha = fecha).filter(id_bloque = bloque).count()
        # cupos del servicio seleccionado
        cupo_servicio = Servicio.objects.filter(id = servicio).values_list('cupo', flat = True)
        cupo_servicio=cupo_servicio[0]
        # total de servicios que hay en esa fecha y bloque
        total_serv=Cita.objects.filter(fecha = fecha).filter(id_bloque = bloque).filter(id_servicio = servicio).count()
        print(total_serv)
        if cupo_bloque < 4:
             print('paso')
             if total_serv < cupo_servicio:
                  print('paso2')
                  if serializer.is_valid(raise_exception= True):
                      serializer.save()
                      subprocess.run(r'C:\Users\metta\Documents\9 semestre\construccion\veterinaria3\veterinaria3\citas\api\correo-cita.py')
                      return Response('Cita agendada con exito')
                  else:
                      return Response('Error')
             else:
                 return Response('No hay cupo para este servicio')     
        return Response('No hay cupos en este horario')

class EliminarCita(APIView):
        @transaction.atomic
        def delete(self,request):
            id_cita = request.query_params['id_cita'] 
            cita = Cita.objects.filter(id= id_cita)
            cita.delete()
            return Response('Cita con eliminada') 
        
class ModificarCita(APIView):
        @transaction.atomic
        def put(self,request):
            id_cita = request.query_params['id_cita']
            cita = Cita.objects.get(id = id_cita)
            serializer = CitaModificarSerializer(cita,request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response('Cita modificada con exito',status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          