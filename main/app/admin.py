from django.contrib import admin
from .models import Car
from .models import Restoration, RangeVoteAdd


admin.site.register(Car)
admin.site.register(Restoration)
admin.site.register(RangeVoteAdd)
