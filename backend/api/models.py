from django.db import models

# Create your models here.

class Admins(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Admins'

    def __str__(self):
        return self.username

class Profesores(models.Model):
    idProfesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=15, unique=True)

    class Meta:
        managed = False
        db_table = 'Profesores'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Secciones(models.Model):
    idSeccion = models.AutoField(primary_key=True)
    anio = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=20)
    idProfesor = models.ForeignKey(Profesores, on_delete=models.CASCADE, db_column='idProfesor')

    class Meta:
        managed = False
        db_table = 'Secciones'

    def __str__(self):
        return f"{self.nombre} - {self.año}"

class Cursos(models.Model):
    idCurso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    idSeccion = models.ForeignKey(Secciones, on_delete=models.CASCADE, db_column='idSeccion')
    idProfesor = models.ForeignKey(Profesores, on_delete=models.CASCADE, db_column='idProfesor')

    class Meta:
        managed = False
        db_table = 'Cursos'

    def __str__(self):
        return self.nombre

class Estudiantes(models.Model):
    idEstudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=15, unique=True)
    idSeccion = models.ForeignKey(Secciones, on_delete=models.CASCADE, db_column='idSeccion')

    class Meta:
        managed = False
        db_table = 'Estudiantes'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Notas(models.Model):
    idNota = models.AutoField(primary_key=True)
    idEstudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE, db_column='idEstudiante')
    idSeccion = models.ForeignKey(Secciones, on_delete=models.CASCADE, db_column='idSeccion')
    idCurso = models.ForeignKey(Cursos, on_delete=models.CASCADE, db_column='idCurso')
    fecha = models.DateField()
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'Notas'

    def __str__(self):
        return f"Nota de {self.idEstudiante} - {self.idCurso}"