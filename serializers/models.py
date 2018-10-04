from django.db import models

def get_ip():
    import socket
    hostname = socket.gethostname()
    return hostname

class Company(models.Model):
    company_id   = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    started_from = models.DateTimeField(auto_now=True)
    country      = models.CharField(max_length=255)
    email        = models.EmailField(max_length=254)
    website      = models.URLField()
    ip           = models.GenericIPAddressField(default=get_ip(),null=True,blank=True)
    active       = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name

class Language(models.Model):
    language_id     = models.BigAutoField(primary_key=True)
    language_name   = models.CharField(max_length=255)
    created_on      = models.DateTimeField(auto_now=True)
    latest_build_on = models.DateTimeField(auto_now_add=True)
    latest_version  = models.DecimalField(max_digits=5, decimal_places=2)
    company         = models.OneToOneField('Company',on_delete=models.CASCADE,related_name='language')

    def __str__(self):
        return self.language_name

class Frameworks(models.Model):
    framework_id    = models.BigAutoField(primary_key=True)
    framework_name  = models.CharField(max_length=255)
    framework_logo  = models.FileField()
    created_on      = models.DateTimeField(auto_now=True)
    latest_build_on = models.DateTimeField(auto_now_add=True)
    latest_version  = models.DecimalField(max_digits=5, decimal_places=2)
    language        = models.ForeignKey('Language',on_delete=models.CASCADE,related_name='frameworks')

    def __str__(self):
        return self.framework_name

class Technologies(models.Model):
    technology_id   = models.BigAutoField(primary_key=True)
    technology_name = models.CharField(max_length=255)
    description     = models.TextField()
    language        = models.ManyToManyField('Language',related_name='technology')

    def __str__(self):
        return self.technology_name
