from django.contrib import admin
from .models import Customer, Address, Enquiry, Order, OrderItem, Product, ProductMaterial, ProductReview, \
    ProductOffer, ProductType, Report, Shipment, ShipmentType, Staff


class CustomerAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


class EnquiryAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderItemAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductMaterialAdmin(admin.ModelAdmin):
    pass


class ProductReviewAdmin(admin.ModelAdmin):
    pass


class ProductOfferAdmin(admin.ModelAdmin):
    pass


class ProductTypeAdmin(admin.ModelAdmin):
    pass


class ReportAdmin(admin.ModelAdmin):
    pass


class ShipmentAdmin(admin.ModelAdmin):
    pass


class ShipmentTypeAdmin(admin.ModelAdmin):
    pass


class StaffAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductMaterial, ProductMaterialAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(ProductOffer, ProductOfferAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(ShipmentType, ShipmentTypeAdmin)
admin.site.register(Staff, StaffAdmin)