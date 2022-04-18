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
    size_length=models.IntegerField(max_length=5)
    size_width=models.IntegerField(max_length=5)
    size_height=models.IntegerField(max_length=5)
    package_type=models.ForeignKey('Package', on_delete=models.PROTECT, null=True)
    directory=models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.title