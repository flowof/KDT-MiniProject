# myApp/admin.py

from django.contrib import admin
# webtoon, user, save 모델 임포트 
from .models import Allwebtoon,member,save

admin.site.register(Allwebtoon)
admin.site.register(member)
admin.site.register(save)

