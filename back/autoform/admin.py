from django.contrib import admin
from .models import (Actions,
                     Operations,
                     Authorisations,
                     Processor)

admin.site.register(Actions)
admin.site.register(Operations)
admin.site.register(Authorisations)
admin.site.register(Processor)