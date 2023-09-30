from rest_framework import serializers
from persona.models import Persona, Cliente,Mascota

class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = ['idusuario','nombre','apellido','email','telefono','password']

    def create(self, validated_data):
        usuario = Persona.objects.create_user(nombre = validated_data['nombre'],apellido=validated_data['apellido']
                                              ,email=validated_data['email'],telefono=validated_data['telefono'],
                                              password=validated_data['password'])
        return usuario

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = ['direccion']


    # def create(self, validated_data):
    #     # persona_data = validated_data.pop('persona')
    #     print(validated_data)
    #     persona_serializer = PersonaSerializer(data=validated_data)
    #     persona_serializer.is_valid(raise_exception=True)
    #     persona = persona_serializer.save()
    #     cliente = Cliente.objects.create(persona=persona, **validated_data)
    #     return cliente
    #     # persona = PersonaSerializer()
    #     # persona_data = validated_data.pop('persona')
    #     # persona = Persona.objects.create(**persona_data)
    #     # cliente = Cliente.objects.create(persona=persona, **validated_data)
    #     # return cliente  
        
class MascotaViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = '__all__'    

class MascotaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = ['nombre','fecha_nacim','especie','raza']

class PersonaSerializerView(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class ClienteViewSerializer(serializers.ModelSerializer):
    persona_idusuario = PersonaSerializerView()
    class Meta:
        model = Cliente
        fields = '__all__'
        
class ClienteVerificacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ['verificado']
        # exclude = ('direccion',)

class CambioPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = ['password']
   
       