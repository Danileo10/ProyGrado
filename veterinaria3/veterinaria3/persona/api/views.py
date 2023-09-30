from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from persona.api.serializers import PersonaSerializer, ClienteViewSerializer, ClienteSerializer,MascotaViewSerializer, MascotaCreateSerializer
from rest_framework.permissions import IsAuthenticated
from persona.models import Persona, Cliente
from django.db import transaction
# from rest_framework_simplejwt import RefreshToken


class guardarPersona(APIView):
    @transaction.atomic
    def post(self,request):
        serializer = PersonaSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            persona = serializer.save()
            serializer2 = ClienteSerializer(data = request.data)
            print(serializer2)
            if serializer2.is_valid(raise_exception=True):
               serializer2.save(persona_idusuario = persona)
            return Response(serializer.data)
        else:
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class clienteView(APIView):
   
    def get(self,request):
        cliente = Cliente.objects.all()
        serializer = ClienteViewSerializer(cliente, many = True)
        
        return Response(serializer.data)

    
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
