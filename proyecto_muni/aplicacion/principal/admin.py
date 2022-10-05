from django.contrib import admin

from.models import Victima
admin.site.register(Victima)


from.models import Agresor
admin.site.register(Agresor)

from.models import Hijos
admin.site.register(Hijos)

from.models import Nota
admin.site.register(Nota)

from.models import Expediente
admin.site.register(Expediente)

from.models import Denuncia
admin.site.register(Denuncia)

from.models import Localidad
admin.site.register(Localidad)

from.models import Tipo
admin.site.register(Tipo)

from.models import Modalidad
admin.site.register(Modalidad)


from.models import Caratula
admin.site.register(Caratula)

from.models import Medida
admin.site.register(Medida)


from.models import Casa_de_proteccion
admin.site.register(Casa_de_proteccion)
# Register your models here.


