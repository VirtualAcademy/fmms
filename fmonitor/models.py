from django.db import models

# Create your models here.
class Userprofile(models.Model):
    userpid
    role
    dob
    address

class Role(models.Model):
    roleid
    rolename
    roledescr


class Product(models.Model):
    pdtid
    pdtname
    pdtdescr
    supplier
    cat
    unitsinstock
    unitsonorder
    pdtavailable
    reorderlevel
    currentorder
    note

class Category(models.Model):
    catid
    catname
    catdescr


class Order(models.Model):
    orderid
    user
    customer
    orderdate
    dispatchdate
    errormsg
    deleted


class OrderDetails(models.Model):
    orddetailid
    order
    product
    ordqty
    delqty
    orderdate
    dispatchdate
    total

class Supplier(models.Model):
    supplerid
    companyname
    address
