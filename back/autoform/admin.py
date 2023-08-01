from django.contrib import admin
from .models import (Actions,
                     Operations,
                     Authorisations)

admin.site.register(Actions)
admin.site.register(Operations)
admin.site.register(Authorisations)