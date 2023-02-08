# myApp/urls.py 

from django.urls import path
from . import views

# 시작페이지 주소와 뷰 함수 연결 
urlpatterns = [
    # 주소 등록 
    # path(주소, views.뷰함수)
    path('', views.index),

    # /myApp/sub1/
    path('sub1/', views.sub1),

    #/myApp/sub2/
    path('sub2/', views.sub2),

    #/myApp/sub3/
    path('sub3/', views.sub3),

    # /myApp/sub4/
    path('sub4/', views.sub4),

    #/myApp/sub5/
    path('sub5/', views.sub5),

    #/myApp/sub6/
    path('sub6/', views.sub6),

    #/myApp/numberCon/
    path('numberCon/', views.numberCon),

    #/myApp/numberCon/
    path('sub7/', views.sub7),

    #/myApp/animalCon/
    path('animalCon/', views.animalCon),

    #/myApp/sub8/
    path('sub8/', views.sub8),

    #/myApp/messageCon/
    path('messageCon/', views.messageCon),

    #/myApp/sub9/
    path('sub9/', views.sub9),

    #/myApp/calculatorCon/
    path('calculatorCon/', views.calculatorCon),

    # /myApp/sub10/
    path('sub10/', views.sub10),

    # /myApp/sub11/
    path('sub11/', views.sub11),

    # /myApp/sub12/
    path('sub12/', views.sub12),

    #학생목록 전체보기
    # /myApp/all/
    path('all/', views.all),

    #학생상세주소
    # /myApp/학생아이디/detail/
    # 예) /myApp/1/detail/
    path('<id>/detail/', views.detail),

    #학생 추가
    # /myApp/register/
    path('register/', views.register),

    #학생 추가 DB 반영
    # /myApp/registerCon/
    path('registerCon/', views.registerCon),

    # 학생 삭제 주소
    # /myApp/학생아이디/wipe/
    # 예) /myApp/1/wipe/
    path('<id>/wipe/', views.wipe),

    # 학생 수정 주소
    # /myApp/학생아이디/modify/
    # 예) /myApp/1/modify/
    path('<id>/modify/', views.modify),

    #학생 수정 사항을 DB 반영
    # /myApp/modifyCon/
    path('modifyCon/', views.modifyCon),

    # city 테이블 모델의 전체 목록 표시 주소
    # /myApp/city/
    path('city/', views.city),




]