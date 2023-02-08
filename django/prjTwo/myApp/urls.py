from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
    path('login/', views.index),
    path('loginCon/', views.loginCon),
    path('user/<id>/', views.user),
    path('user/<id>/search/', views.search),
    path('user/<id>/search/<webtoon>/createCon/', views.createSearchCon),
    path('user/<id>/search/<webtoon>/deleteCon/', views.deleteSearchCon),
    path('user/<id>/webtoon/<webtoon>/', views.webtoon),
    path('user/<id>/webtoon/<webtoon>/create/', views.createComment),
    path('user/<id>/webtoon/<webtoon>/createCon/', views.createCommentCon),
    path('user/<id>/webtoon/<webtoon>/update/', views.updateComment),
    path('user/<id>/webtoon/<webtoon>/updateCon/', views.updateCommentCon),
    path('user/<id>/webtoon/<webtoon>/deleteCon/', views.deleteCommentCon),
    path('user/<id>/<week>/', views.userWeek),

]