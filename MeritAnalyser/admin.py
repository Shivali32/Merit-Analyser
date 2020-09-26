from django.contrib import admin
from MeritAnalyser.models import UserDetails,Teacher,Student,Test,Class

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
'''admin.site.register(Subject)'''
admin.site.register(Test)
admin.site.register(Class)
admin.site.register(UserDetails)