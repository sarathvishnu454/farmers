from django.contrib import admin
from .models import friends, imagedetails, farmers, articles


# Register your models here.
class friendsadmin(admin.ModelAdmin):
    model = 'friends'
    list_display = ['name', 'age', 'place']
    list_editable = ('age', 'place')
    list_filter = ('place',)
admin.site.register(friends, friendsadmin)

class imageadmin(admin.ModelAdmin):
    model = 'imagedetails'
    list_display = ['name', 'age', ]
    list_editable = ('age',)
admin.site.register(imagedetails, imageadmin)

class farmersadmin(admin.ModelAdmin):
    model = 'farmers'
    list_display = ['image', 'name', 'Designation']
    list_editable = ('name','Designation')
admin.site.register(farmers, farmersadmin)

class articlesadmin(admin.ModelAdmin):
    model = 'articles'
    list_display = ['image','description','date']
    list_editable = ('description','date')
admin.site.register(articles,articlesadmin)

