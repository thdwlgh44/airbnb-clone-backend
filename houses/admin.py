from django.contrib import admin
from .models import House

# Register your models here.
# admin 패널에 House라는 model을 등록
@admin.register(House) 
class HouseAdmin(admin.ModelAdmin):

    # fields = ("name", "address", ("price_per_night", "pets_allowed"),)
    list_display = ("name", "price_per_night", "address", "pets_allowed")
    list_filter = ("price_per_night", "pets_allowed")
    # search_fields = ("address",) # 여기에 들어간 텍스트로 시작하는 것만 검색한다. tuple에 element가 하나만 있으면 ,를 붙여줘야 한다.
    # exclude = ("price_per_night",)
    # list_display_links = ("name", "address")
    # list_editable = ("pets_allowed",)
