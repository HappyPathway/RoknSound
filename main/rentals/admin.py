from django.contrib import admin

# Register your models here.
from rentals.models import Equipment, EquipmentAccessory, EquipmentType, EquipmentMedia, EquipmentStatus

class EquipmentAdmin(admin.ModelAdmin):
    pass

class EquipmentTypeAdmin(admin.ModelAdmin):
    pass

class EquipmentAccessoryAdmin(admin.ModelAdmin):
    pass

class EquipmentMediatAdmin(admin.ModelAdmin):
    pass


admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(EquipmentAccessory, EquipmentAccessoryAdmin)
admin.site.register(EquipmentMedia, EquipmentMediatAdmin)
admin.site.register(EquipmentType, EquipmentTypeAdmin)
admin.site.register(EquipmentStatus, EquipmentAdmin)