from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'myApp/login.html')

def loginCon(request):
    email = request.POST['email']
    # DB에서 email select 하고, 없으면 insert 후에 ID 값 가져오기
    id = 1
    return redirect(f'/user/{id}/')

def user(request, id):
    # DB에서 ID 값으로 전체 저장 목록 가져오기
    context = {
        'id': id
    }
    return render(request, 'myApp/user.html', context)

def userWeek(request, id, week):
    # DB에서 ID 값으로 요일 저장 목록 가져오기
    context = {
        'id': id,
        'week': week
    }
    return render(request, 'myApp/user.html', context)

def search(request, id):
    context = {
        'id': id
    }
    try:
        search = request.GET['search']
        # DB에서 작품명 또는 작가명으로 검색
    except:
        search = ''
    context = {
        'id': id,
        'search': search
    }
    return render(request, 'myApp/search.html', context)

def createSearchCon(request, id, webtoon):
    # 웹툰 저장
    return redirect(f'/user/{id}/')

def deleteSearchCon(request, id, webtoon):
    # 웹툰 삭제
    return redirect(f'/user/{id}/')

def webtoon(request, id, webtoon):
    # webtoon으로 작품 검색
    context = {
        'id': id,
        'webtoon': webtoon
    }
    return render(request, 'myApp/webtoon.html', context)

def createComment(request, id, webtoon):
    context = {
        'id': id,
        'webtoon': webtoon
    }
    return render(request, 'myApp/createComment.html', context)

def createCommentCon(request, id, webtoon):
    # id, webtoon으로 코멘트 수정
    context = {
        'id': id,
        'webtoon': webtoon,
    }
    return redirect(f'/user/{id}/webtoon/{webtoon}/')

def updateComment(request, id, webtoon):
    # id, webtoon으로 코멘트 검색
    context = {
        'id': id,
        'webtoon': webtoon,
        'comment': 'Test'
    }
    return render(request, 'myApp/updateComment.html', context)

def updateCommentCon(request, id, webtoon):
    # id, webtoon으로 코멘트 수정
    context = {
        'id': id,
        'webtoon': webtoon,
    }
    return redirect(f'/user/{id}/webtoon/{webtoon}/')

def deleteCommentCon(request, id, webtoon):
    # id, webtoon으로 코멘트 삭제
    return redirect(f'/user/{id}/webtoon/{webtoon}/')