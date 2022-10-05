from django.db import models

class Nota(models.Model):
	fecha_de_ingreso=models.DateField(max_length=100)
	institucion=models.CharField(max_length=100)


class Victima(models.Model):
	dni_victima=models.CharField(max_length=100, primary_key=True)
	nombre=models.CharField(max_length=100)
	apellido=models.CharField(max_length=100)
	documento=models.CharField(max_length=10)
	telefono=models.CharField(max_length=20)
	direccion=models.CharField(max_length=100)
	codigo_postal=models.CharField(max_length=10)
	fecha_de_nacimiento=models.DateField(max_length=100)


class Agresor(models.Model):
	dni_agresor=models.CharField(max_length=100)
	nombre=models.CharField(max_length=100)
	apellido=models.CharField(max_length=100)
	documento=models.CharField(max_length=100)
	telefono=models.CharField(max_length=100)
	direccion=models.CharField(max_length=100)
	codigo_postal=models.CharField(max_length=100)
	fecha_de_nacimiento=models.DateField(max_length=100)


class Hijos(models.Model):
	dni_hijos=models.CharField(max_length=100)
	nombre=models.CharField(max_length=100)
	apellido=models.CharField(max_length=100)
	fecha_de_nacimiento=models.DateField(max_length=100)


class Expediente(models.Model):
	fecha_expediente=models.CharField(max_length=100)
	numero_expediente=models.CharField(max_length=100)
	


class Localidad(models.Model):
	direccion=models.CharField(max_length=100)
	barrio=models.CharField(max_length=100)


class Denuncia(models.Model):
	numero_expediente=models.CharField(max_length=100)
	id_modalidad=models.CharField(max_length=100)
	id_tipo=models.CharField(max_length=100)

class Tipo(models.Model):

	id_tipo=models.CharField(max_length=100)


class Modalidad(models.Model):

	id_modalidad=models.CharField(max_length=100)
	

class Caratula(models.Model):
	 
	id_caratula=models.CharField(max_length=100)


class Periodo(models.Model):
	año=models.CharField(max_length=100)
	fecha_de_recepcion=models.CharField(max_length=100)
	fechaa_medida_de_plazo=models.CharField(max_length=100)
	numero_expediente=models.CharField(max_length=100)



class Medida(models.Model):
	id_caratula=models.CharField(max_length=100)
	numero_expediente=models.CharField(max_length=100)
	dni_victima=models.CharField(max_length=100)
	dni_agresor=models.CharField(max_length=100)
	resolucion=models.CharField(max_length=100)
	alcance=models.CharField(max_length=100)



class Casa_de_proteccion(models.Model):
	id_casa_proteccion=models.CharField(max_length=100)
	nombre=models.CharField(max_length=100)

