from django.contrib import admin

from bitfield import BitField
from bitfield.forms import BitFieldCheckboxSelectMultiple

from bitfield.admin import BitFieldListFilter

from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        BitField: {'widget': BitFieldCheckboxSelectMultiple}
    }

    list_filter = (
        ('flags', BitFieldListFilter),
    )
admin.site.register(MyModel, MyModelAdmin)
