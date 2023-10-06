from django.db import models
class datetime1(models.Model):
    time12=models.TextField(max_length=255,null=False,default=None)
    class Meta:
        db_table="datetime1"

class contactus(models.Model):
    firstname=models.TextField(max_length=255,null=False,default=None)
    lastname = models.TextField(max_length=255,null=False,default=None)
    email = models.EmailField(max_length=255,null=False,default=None)
    comment = models.TextField(max_length=255,null=False,default=None)
    class Meta:
        db_table="contactus"

class signingup(models.Model):
    fname = models.TextField(max_length=255,null=False,default=None)
    lname = models.TextField(max_length=255,null=False,default=None)
    gmail = models.EmailField(max_length=255,null=False,default=None)
    mobile = models.BigIntegerField(null=False, default=None)
    uname = models.TextField(max_length=255, null=False, default=None)
    psswrd = models.TextField(max_length=255, null=False, default=None)
    class Meta:
        db_table="signingup"