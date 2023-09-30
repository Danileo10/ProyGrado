from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from persona.api.serializers import PersonaSerializer, ClienteViewSerializer, ClienteSerializer,MascotaViewSerializer, MascotaCreateSerializer, ClienteVerificacionSerializer
from rest_framework.permissions import IsAuthenticated
from persona.models import Persona, Cliente
from django.db import transaction
import subprocess 
from django.contrib.auth.models import User
# from rest_framework_simplejwt import RefreshToken


class guardarPersona(APIView):
    @transaction.atomic
    def post(self,request):
        serializer = PersonaSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            persona = serializer.save()
            serializer2 = ClienteSerializer(data = request.data)
            if serializer2.is_valid(raise_exception=True):
               serializer2.save(persona_idusuario = persona)
               subprocess.run(["python", r"C:\Users\danil\OneDrive\Escritorio\proyectoGrado\veterinaria2-pruebas\veterinaria2-pruebas\persona\api\correo-ver.py"])
            return Response(serializer.data)
        else:
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class clienteView(APIView):
   
    def get(self,request):
        cliente = Cliente.objects.all()
        serializer = ClienteViewSerializer(cliente, many = True)
        
        return Response(serializer.data)

class ClienteVerificacion(APIView):
   @transaction.atomic
   def put(self,request):
      id_cliente = request.query_params['id_cliente']
      cliente = Cliente.objects.get(idcliente = id_cliente)
      estado = Cliente.objects.filter(idcliente = id_cliente).values_list('verificado', flat=True)
      estado = estado[0]
      if estado == False:
         data = {"verificado": 1}
         serializer = ClienteVerificacionSerializer(cliente,data=data)
         if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Cliente verificado',status=status.HTTP_200_OK)
         else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
      else:
         return Response('Cuenta ya verificada', status=status.HTTP_403_FORBIDDEN)   


class CorreoPassword(APIView):
   def get(self,request):
      subprocess.run(["python", r"C:\Users\metta\Documents\9 semestre\construccion\veterinaria3\veterinaria3\persona\api\correo-pass.py"])
      return Response(status=status.HTTP_200_OK)


class CambiarContraseña(APIView):
   @transaction.atomic
   def patch(self,request):
      id_cliente = request.query_params['id_cliente']
      cliente = Persona.objects.get(idusuario=id_cliente)
      print(cliente)
      contraseña = request.POST['contraseña']
      print(contraseña)
      contraseña = cliente.set_password(contraseña)
      print(cliente)
      print(contraseña)

    
class MascotaCreate(APIView):
   @transaction.atomic
   def post(self,request):
      id_cliente = request.query_params['id_cliente']
      serializer = MascotaCreateSerializer(data=request.data)
      cliente = Cliente.objects.get(idcliente = id_cliente)
      if serializer.is_valid(raise_exception=True):
         serializer.save(id_clienteid = cliente)
         return Response(serializer.data)
      else:
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class LogoutView(APIView):
#      permission_classes = (IsAuthenticated,)
#      def post(self, request):
          
#           try:
#                refresh_token = request.data["refresh_token"]
#                token = RefreshToken(refresh_token)
#                token.blacklist()
#                return Response(status=status.HTTP_205_RESET_CONTENT)
#           except Exception as e:
#                return Response(status=status.HTTP_400_BAD_REQUEST)   
