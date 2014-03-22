from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    addressId = models.ForeignKey(Address, null=True)
    telephone = models.CharField(max_length=100)


class ProductMaterial(models.Model):
    type = models.CharField(max_length=100)


class ProductReview(models.Model):
    text = models.CharField(max_length=4000)
    created = models.DateTimeField(auto_now_add=True)
    customerId = models.ForeignKey(Customer, null=True)


class ProductOffer(models.Model):
    type = models.CharField(max_length=100)


class ProductType(models.Model):
    type = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    picturePath = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    materialId = models.ForeignKey(ProductMaterial, null=True)
    typeId = models.ForeignKey(ProductType, null=True)
    isBroken = models.BooleanField()
    brokenQuantity = models.IntegerField()
    offerId = models.ForeignKey(ProductOffer, null=True)
    reviewId = models.ForeignKey(ProductReview, null=True)


class OrderItem(models.Model):
    productId = models.ForeignKey(Product, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()


class Order(models.Model):
    orderItemId = models.ForeignKey(OrderItem, null=True)
    created = models.DateTimeField(auto_now_add=True)
    subtotal = models.FloatField()
    total = models.FloatField()
    isDone = models.BooleanField()
    customerId = models.ForeignKey(Customer, null=True)


class Enquiry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    customerId = models.ForeignKey(Customer, null=True)
    subject = models.CharField(max_length=100)
    content = models.CharField(max_length=4000)
    response = models.CharField(max_length=4000)
    isDone = models.BooleanField()


class Report(models.Model):
    filePath = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


class ShipmentType(models.Model):
    type = models.CharField(max_length=100)
    price = models.FloatField()


class Shipment(models.Model):
    typeId = models.ForeignKey(ShipmentType, null=True)
    created = models.DateTimeField(auto_now_add=True)
    addressId = models.ForeignKey(Address, null=True)


class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    isDirector = models.BooleanField()
