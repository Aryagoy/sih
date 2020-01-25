from django.contrib import admin

# Register your models here.
from .models import vital
from .models import chronic
from .models import accident_insurance
from .models import general_details
from .models import registration
from .models import chronic_month2
from .models import chronic_month3
from .models import vital2
from .models import vital3
from .models import ocr


admin.site.register(vital)
admin.site.register(chronic)
admin.site.register(accident_insurance)
admin.site.register(general_details)
admin.site.register(registration)
admin.site.register(chronic_month2)
admin.site.register(chronic_month3)
admin.site.register(vital2)
admin.site.register(vital3)
admin.site.register(ocr)
