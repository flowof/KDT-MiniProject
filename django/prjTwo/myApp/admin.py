# myApp/admin.py

from django.contrib import admin
# webtoon, user, save 모델 임포트 
from .models import webtoon, user, save

admin.site.register(webtoon)
admin.site.register(user)
admin.site.register(save)