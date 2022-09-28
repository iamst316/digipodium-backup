from django.contrib import admin
from .models import Movies, Show, Student, Report, Weather
# Register your models here.
admin.site.register(Movies)
admin.site.register(Show)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    '''Admin View for Student'''

    list_display = ('rollno','name','klass')
    search_fields = ('name','klass')
    
    ordering = ('name',)