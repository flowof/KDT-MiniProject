# myApp/models.py

from django.db import models

# 학생 테이블 모델 정의 
# class 테이블모델명(models.Model)
#   필드명 = models.자료형(옵션)
class Student(models.Model):
    s_name = models.CharField(max_length=100)
    s_major = models.CharField(max_length=100)
    s_age = models.IntegerField(default=0)
    s_grade = models.IntegerField(default=0)
    s_gender = models.CharField(max_length=10)

    def __str__(self):
        return self.s_name


# City 테이블 모델 정의 
class City(models.Model):
    name = models.CharField(max_length=100)   # 도시명 
    population = models.IntegerField(default=0)  # 인구수 

    def __str__(self):
        return self.name
