from django.db import models



class Equipment_type(models.Model):
    title=models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.title


class Client(models.Model):
    title = models.CharField(max_length=100)
    slug=models.SlugField(max_length=255, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.title

class Package(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.title

class Equipment(models.Model):
    articul=models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=100, null=True)
    client = models.ForeignKey('Client', on_delete=models.PROTECT, null=True)
    type = models.ForeignKey('Equipment_type', on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', null=True)
    size_length=models.IntegerField()
    size_width=models.IntegerField()
    size_height=models.IntegerField()
    package_type=models.ForeignKey('Package', on_delete=models.PROTECT, null=True)
    directory=models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.title



class DkoEmployer(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    status=models.BooleanField(default=True)
    # position=models.ForeignKey('Staff_position', on_delete=models.PROTECT, null=True)
    def __str__(self):
        return (f'{self.surname} {self.name}')

class MarketEmployer(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    status=models.BooleanField(default=True)
    initials=models.CharField(max_length=5, null=True)
    # position=models.ForeignKey('Staff_position', on_delete=models.PROTECT, null=True)
    def __str__(self):
        return (f'{self.surname} {self.name}')




class Tasks(models.Model):
    numder=models.CharField(max_length=10)
    suffix=models.CharField(max_length=10)
    manager=models.ForeignKey('MarketEmployer', on_delete=models.PROTECT, null=True)
    executor=models.ForeignKey('DkoEmployer', on_delete=models.PROTECT, null=True)
    description=models.TextField(max_length=500)

    def __str__(self):
        return self.numder,self.suffix,self.manager

