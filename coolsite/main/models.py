from django.db import models
from django.urls import reverse



class SideBar(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse ()

class ProductionCats(models.Model):
    cats=models.CharField(max_length=20)
    menu = models.ForeignKey('SideBar', on_delete=models.PROTECT, null=True)


class ProductionInfo(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='photo/%Y/%m/%d/', null=True)
    menu=models.ForeignKey('ProductionCats', on_delete=models.PROTECT, null=True)


class AboutCompany(models.Model):
    info=models.CharField(max_length=200)
    menu = models.ForeignKey('SideBar', on_delete=models.PROTECT, null=True)

class Blogs(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', null=True)
    time_create=models.DateTimeField(auto_now_add=True)
    is_published=models.BooleanField(default=True)
    menu = models.ForeignKey('SideBar', on_delete=models.PROTECT, null=True)

class Contacts(models.Model):
    name=models.CharField(max_length=60)
    post=models.CharField(max_length=60)
    contacts=models.CharField(max_length=60)
    menu = models.ForeignKey('SideBar', on_delete=models.PROTECT, null=True)
