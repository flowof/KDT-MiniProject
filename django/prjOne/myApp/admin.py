# myApp/admin.py

from django.contrib import admin
# Student, City 모델 임포트 
from .models import Student, City

# Register your models here.
# 관리자페이지에 Student, City 모델추가 
# admin.site.register(모델명)
admin.site.register(Student)
admin.site.register(City)