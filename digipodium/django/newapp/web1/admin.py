from django.contrib import admin
from .models import Artist, Movies, Show, Song, Student, Report, Weather
# Register your models here.
admin.site.register(Movies)
admin.site.register(Show)
admin.site.register(Report)
admin.site.register(Weather)
admin.site.register(Artist)
admin.site.register(Song)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    '''Admin View for Student'''

    list_display = ('rollno','name','klass')
    search_fields = ('name','klass')
    
    ordering = ('name',)