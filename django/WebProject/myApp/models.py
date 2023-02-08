# myApp/models.py

from django.db import models


# 웹툰데이터


class Allwebtoon(models.Model):
    id = models.IntegerField(primary_key='True')
    week = models.CharField(max_length=100) # 요일
    title = models.CharField(max_length=100) # 제목
    URL = models.TextField("Site URL") # url
    thumbnail = models.TextField("Site THUMB") # 썸네일url
    author = models.CharField(max_length=100) # 작가
    summary = models.TextField() # 줄거리
    genre = models.CharField(max_length=100) # 장르
    age = models.CharField(max_length=100) # 연령제한
    company = models.CharField(max_length=100) # 웹툰제작사?

    def __str__(self):
        return self.title

# 이메일데이터
class member(models.Model):
    # id = models.IntegerField(primary_key='True') 
    email = models.EmailField(max_length=128, verbose_name="사용자 이메일", unique='email') # 이메일

    def __str__(self):
        return self.email

# 웹툰저장데이터
class save(models.Model):
    memberid = models.IntegerField(default=0) #유저번호
    webtoonid = models.TextField() #웹툰 아이디
    comment = models.TextField() # 웹툰코멘트
    
    def __str__(self):
        return self.webtoonid


