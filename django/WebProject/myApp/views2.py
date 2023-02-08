from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Allwebtoon,member,save
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'myApp/login.html')

def loginCon(request):
    email = request.POST['email']


    Member, _ = member.objects.get_or_create(
        email=email
    )

    # Save, _ = save.objects.get_or_create(
    #     meberid = 

    # )


    return redirect(f'/user/{Member.id}/')

def user(request, id):
    # DB에서 ID 값으로 전체 저장 목록 가져오기                =>id값으로 데이터베이스 저장 목록 연결 코드 짜기
    save_list = member.objects.get(id=id)


    # save_list = 'Hi'
    # a = []

    # for i in Save:
    #     a.append()
    
    # webtoon 
    
    context = {
        'save_list1': save_list
        
    }


    return render(request, 'myApp/user.html', context)



def userWeek(request, id, week):

    # DB에서 ID 값으로 요일 저장 목록 가져오기           => 요일 확인 요일 컬럼 .join 확인

    # save  - > memberid (전체 가지고 와서) - > webtoonid 요소들 연결 - > webtoonid ->
    # save_list = save.objects.get(memberid=id)
    
    
    context = {
        'id': id,
        'week': week
    }
    return render(request, 'myApp/user.html', context)




def search(request, id):



    context = {
        'id': id
    }

    # search_list = Allweb.objects.get(id=id)

    # try:
        # search = request.GET['search']     #글자 입력받고 select == 같은걸찾는거네요. 리스트로 반환해서 화면에 나오게끔
        # DB에서 작품명 또는 작가명으로 검색
    try :
        search_word = request.GET['search']
        search_list = Allwebtoon.objects.filter(Q(title=search_word)).distinct()


    # search_list = webtoon.objects.filter(title=search_word)

        # search_list = webtoon.objects.get(title=search_word)
        
    except:
        search_list = '하이'


    # webtoon 테이블에 접근 - > title에 접근해서 값이랑 맞으면 webtoon 아이디 값 출력
    #  테이블에 특정 요소가 있으면 그것을 가지고 와라 라는 구문.


    context = {
        'id': id,
        'Search': search_list
    }


    return render(request, 'myApp/search.html', context)



def createSearchCon(request, id, webtoon):    #insert 저장   코드를 만들어서  insert 저장하게끔.

    # 웹툰 저장
    return redirect(f'/user/{id}/')




def deleteSearchCon(request, id, webtoon):   #삭제 되게끔.
    # 웹툰 삭제
    return redirect(f'/user/{id}/')




def webtoon(request, id, webtoon):             #저장된것 상세보기 (다른 키워드들 불러와야겠네.)    
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

def createCommentCon(request, id, webtoon):  # 다른 테이블 id 로 들어가기.
    # id, webtoon으로 코멘트 입력
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