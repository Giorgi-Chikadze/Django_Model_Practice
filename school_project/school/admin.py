from django.contrib import admin

from school.models import Students, Teacher, Class

admin.site.register(Students)
admin.site.register(Teacher)
admin.site.register(Class)