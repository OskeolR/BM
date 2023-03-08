from django.contrib import admin
from MaleApp import models
from .models import *


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Product_female)
admin.site.register(Footer)
admin.site.register(Contact)
admin.site.register(Payment)
admin.site.register(Subscribe)
admin.site.register(RegisterUser)
admin.site.register(Unique_ProductMale)
admin.site.register(Unique_ProductFemale)
admin.site.register(P_F_images)
admin.site.register(P_M_images)
admin.site.register(Orders_male)
admin.site.register(Orders_female)