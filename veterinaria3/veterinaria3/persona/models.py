from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class PersonaManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, telefono, password=None):
        if not email:
            raise ValueError('Los usuarios deben tener una dirección de correo electrónico')
        if not password:
            raise ValueError("Debes digitar una contraseña")
        if not nombre:
            raise ValueError("Debes digitar un nombre")
        if not apellido:
            raise ValueError("Debes digitar un apellido")
        if not telefono:
            raise ValueError("Debes digitar un telefono")


        # usuario = self.model(
        #     email=self.normalize_email(email),
        #     nombre=nombre,
        #     apellido=apellido,
        #     telefono=telefono
        usuario = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            password=make_password(password)
        )

        # usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, email, nombre, apellido, telefono, password):
        usuario = self.create_user(
            email=self.normalize_email(email),
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            password=password
        )
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario

class Persona(AbstractBaseUser):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=45)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False) 

    objects = PersonaManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'telefono','password']

    class Meta:
        db_table = 'persona_persona'


# class Persona(AbstractBaseUser):
#     idusuario = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=45)
#     apellido = models.CharField(max_length=45)
#     email = models.EmailField(unique=True)
#     telefono = models.CharField(max_length=45)
#     contraseña = models.CharField(max_length=45)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']


class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=45)
    persona_idusuario = models.ForeignKey(Persona, on_delete=models.CASCADE)     

class Mascota(models.Model):
    idmascota = models.AutoField(primary_key=True)
    id_clienteid = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_clienteid_id')
    nombre = models.CharField(max_length=45)
    fecha_nacim = models.DateField()
    especie = models.CharField(max_length=45)
    raza = models.CharField(max_length=45)
    fecha_defun = models.DateField(null = True,blank=False)


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    persona_idusuario = models.ForeignKey(Persona, on_delete=models.CASCADE)