from django.contrib import admin

from petbay.models.accessory_models import Accessory
from authentication.models.auth_models import User
from petbay.models.feed_models import Feed
from petbay.models.medication_models import Medication
from petbay.models.pet_models import PetType, Pet
from petbay.models.transaction_models import Transaction


# Register your models here
# Admin customization
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pet_type', 'price', 'is_available')

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_available')

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_available')

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_available')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'item_type', 'price', 'buyer', 'date_purchased')