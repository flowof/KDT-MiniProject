# myApp/models.py

from django.db import models


# 웹툰데이터
class webtoon(models.Model):
    week = models.CharField(max_length=100) # 요일
    title = models.CharField(max_length=100) # 제목
    URL = models.TextField("Site URL") # url
    thumbnail = models.TextField("Site THUMB") # 썸네일url
    author = models.CharField(max_length=100) # 작가
    summary = models.TextField() # 줄거리
    genre = models.CharField(max_length=100) # 장르
    age = models.IntegerField(default=0) # 연령

    def __str__(self):
        return self.name

# 이메일데이터
class user(models.Model):
    email = models.CharField(max_length=100) # 이메일
    
    def __str__(self):
        return self.name

# 웹툰저장데이터
class save(models.Model):
    userid=models.IntegerField(default=0) #유저번호
    webtoonid = models.TextField() #웹툰 아이디
    comment = models.TextField() # 웹툰코멘트
    
    def __str__(self):
        return self.name