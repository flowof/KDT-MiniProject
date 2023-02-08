from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from .models import Allwebtoon,member,save
from django.db.models import Q
# Create your views here.
memberid = ''
memberemail = ''
def index(request):
    global memberid
    return render(request, 'myApp/login.html')

def loginCon(request):
    global memberemail
    global memberid
    email = request.POST['email']

   

    Member, _ = member.objects.get_or_create(
        email=email
    )

    user = member.objects.get(email=email)
    memberid = user.id
    memberemail = email


    # DB에서 email select 하고, 없으면 insert 후에 ID 값 가져오기
    
    return redirect(f'/user/')

def user(request):
    # DB에서 ID 값으로 전체 저장 목록 가져오기
    global memberid
    global memberemail


    save_list = save.objects.filter(memberid=memberid)
    webtoon_list = []
    for content in save_list:
        try:
            webtoon_list.append(Allwebtoon.objects.get(id = content.webtoonid))
        except:
            pass

    context = {
        'memberid': memberid,
        'memberemail': memberemail,
        'webtoon_list': webtoon_list
    }
    return render(request, 'myApp/user.html', context)

def userWeek(request, week):

    # DB에서 ID 값으로 요일 저장 목록 가져오기
    global memberid
    global memberemail
    day = week
    save_list = save.objects.filter(memberid=memberid)
    webtoon_list = []
    for content in save_list:
        try:
            webtoon_list.append(Allwebtoon.objects.get(Q(id = content.webtoonid) & Q(week = day)))
        except:
            pass

    context = {
        'memberid': memberid,
        'memberemail': memberemail,
        'week': week,
        'webtoon_list': webtoon_list
    }
    # return HttpResponse(save_list)
    return render(request, 'myApp/user.html', context)

def search(request):
    global memberid

    context = {
        'memberid': memberid
    }
    try :
        search_word = request.GET['search']
        search_list = Allwebtoon.objects.filter(Q(title__contains=search_word) | Q(author__contains = search_word)).distinct() 
        # search_list = webtoon.objects.filter(title=search_word)

        # search_list = webtoon.objects.get(title=search_word)
        
    except:
        search_word = ''
        search_list = []
        

    context = {
        'memberid': memberid,
        'word' : search_word,
        'search': search_list
    }
    return render(request, 'myApp/search.html', context)


def createSearchCon(request, webtoonid):
    global memberid
    
    save_webtoon, _ = save.objects.get_or_create(
        memberid = memberid,
        webtoonid = webtoonid
    )
    
    # 웹툰 저장
    return redirect(f'/user/')

def deleteSearchCon(request, webtoonid):
    global memberid
    save_data = save.objects.get(Q(memberid=memberid) & Q( webtoonid = webtoonid))
    save_data.delete()

    return redirect(f'/user/')

def webtoon(request, webtoonid):
    # webtoon으로 작품 검색
    global memberid
    save_data = save.objects.get(Q(memberid=memberid) & Q( webtoonid = webtoonid))
    webtoon_data = Allwebtoon.objects.get(id = webtoonid)
    context = {
        'save_data': save_data,
        'webtoon_data': webtoon_data
    }
    return render(request, 'myApp/webtoon.html', context)

def createComment(request, webtoonid):
    global memberid
    context = {
        'memberid': memberid,
        'webtoonid': webtoonid
    }
    return render(request, 'myApp/createComment.html', context)

def createCommentCon(request, webtoonid):
    # id, webtoonid으로 코멘트 수정
    global memberid
    comment = request.GET['comment']
    save_data = save.objects.get(Q(memberid = memberid) & Q(webtoonid = webtoonid))
    save_data.comment = comment
    save_data.save()
   
    return redirect(f'/user/webtoon/{webtoonid}/')

def updateComment(request, webtoonid):
    # id, webtoonid으로 코멘트 검색
    global memberid
    save_data = save.objects.get(Q(memberid = memberid) & Q(webtoonid = webtoonid))
    context = {
        'memberid': memberid,
        'webtoonid': webtoonid,
        'save_data': save_data
    }
    return render(request, 'myApp/updateComment.html', context)

def updateCommentCon(request, webtoonid):
    # id, webtoonid으로 코멘트 수정
    global memberid
    comment = request.GET['comment']
    save_data = save.objects.get(Q(memberid = memberid) & Q(webtoonid = webtoonid))
    save_data.comment = comment
    save_data.save()

    return redirect(f'/user/webtoon/{webtoonid}/')

def deleteCommentCon(request, webtoonid):
    global memberid
    save_data = save.objects.get(Q(memberid = memberid) & Q(webtoonid = webtoonid))
    save_data.comment = ''
    save_data.save()
    # id, webtoonid으로 코멘트 삭제
    return redirect(f'/user/webtoon/{webtoonid}/')