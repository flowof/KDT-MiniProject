from django.shortcuts import redirect, render
# 추가
from django.http import HttpResponse
# Student, City 모델 임포트 추가
from .models import Student, City
# 추가
from django.shortcuts import redirect

# /, /myApp/ 주소와 연결되는 뷰함수
def index(request):
    return HttpResponse("<h1>Hello world</h1>")

# /myApp/sub1 주소와 연결되는 뷰함수
def sub1(request):
    return render(request, 'myApp/sub1.html')

# /myApp/sub2 주소와 연결되는 뷰함수
def sub2(request):
    return render(request, 'myApp/sub2.html')
    
# /myApp/sub3 주소와 연결되는 뷰함수
def sub3(request):
    # 딕셔너리 형태로 전송 데이터 정의
    context = {
        'name': '공지철',
        'id' : 'YYY',
        'age' : 40,
        'grade' : [90, 85, 77]

    }
    return render(request, 'myApp/sub3.html', context)

# /myApp/sub4 주소와 연결되는 뷰함수
def sub4(request):

    # 리스트안에 튜플로 정의 => 튜플리스트 2차원
    # 4행 2열 스타일
    book_info = [
        ('title', '어린왕자'),
        ('writer', '생텍쥐페리'),
        ('price', 15000),
        ('ISBN', '483731-849-90'),
    ]

    # 5행 4열 스타일
    student_info = [
        ('홍길동', '남', '부산', 23),
        ('고길동', '남', '전주', 28),
        ('윤길동', '남', '서울', 23),
        ('박길동', '남', '마산', 23),
        ('정길순', '여', '울산', 22),
    ]

    # 딕셔너리 형태로 전송 데이타 정의 
    context = {
           'book_info': book_info, 
           'student_info' :  student_info,
           'numList' : range(1,11), # [1, 2, ... 10]
    }

    return render(request, 'myApp/sub4.html', context)

# /myApp/sub5 주소와 연결되는 뷰함수
def sub5(request):
    # 책제목과 가격으로 구성된 튜플 리스트 생성
    book_list = [
        ('파이썬 도장', 33000),
        ('C언어', 23000),
        ('JAVA', 43000),
    ]
    context = { 
                'book_list':book_list ,
            }
    return render(request, 'myApp/sub5.html', context)

    # myApp/sub6 주소와 연결되는 뷰함수
def sub6(request):
    return render(request, 'myApp/sub6.html')

# /myApp/numberCon 주소와 연결되는 뷰함수
def numberCon(request):
    # 폼에서 GET 방식으로 전달받은 데이터를 번수에 저장
    number = request.GET['number']
    try:
        number = int(number)
    except:
        result = '입력값은 숫자가 아닙니다'
    else:
        if number%2 ==0:
            result = '짝수'
        else:
            result = '홀수'


    context = {
        'number' : number,
        'result' : result,
    }
    #return HttpResponse(result)
    return render(request, 'myApp/sub6_result.html',context)
    
# myApp/sub7 주소와 연결되는 뷰함수
def sub7(request):
    return render(request, 'myApp/sub7.html')

# /myApp/animalCon 주소와 연결되는 뷰함수
def animalCon(request):
    # GET 방식으로 전달받은 데이타를 변수에 저장 
    birth = request.GET['birth']

    # 태어난년도%12 알고리즘을 위한 띠 리스트 정의 
    animal_list = ['원숭이', '닭', '개', '돼지', '쥐', '소',
                 '범', '토끼', '용', '뱀', '말', '양']
    
    idx = int(birth)%12
    result = animal_list[idx]

    context = { 
                'birth':birth , 
                'result':result,
                }

    # return HttpResponse(result)
    return render(request, 'myApp/sub7_result.html', context)   

# /myApp/sub8 주소와 연결되는 뷰함수
def sub8(request):
    return render(request, 'myApp/sub8.html')   

# /myApp/sub8 주소와 연결되는 뷰함수
def messageCon(request):
    # POST 방식으로 전달받은 데이터를 변수에 저장
    userName = request.POST['userName']
    # result = userName + '님... 오늘도 편안한 하루 되세요...'
    # f'문자열....{변수명} 문자열.....'
    result = f'{userName}님... 오늘도 편안한 하루 되세요...'
    context = {
        'result' : result,
    }
    return render(request, 'myApp/sub8_result.html', context)

# myApp/views.py 

# /myApp/sub9 주소와 연결되는 뷰함수
def sub9(request):
    return render(request, 'myApp/sub9.html')  

# /myApp/calculatorCon 주소와 연결되는 뷰함수
def calculatorCon(request):
    # POST 방식으로 전달받은 데이타를 변수에 저장 
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    if num2 != 0:
        result4 = f'{num1} / {num2} = {round(num1/num2,2)}'
    else:
        result4 = '0으로 나눌 수 없어요...'

    context = {
        'result1':f'{num1} + {num2} = {num1+num2}',
        'result2':f'{num1} - {num2} = {num1-num2}',
        'result3':f'{num1} * {num2} = {num1*num2}',
        # round(계산결과, 소숫점자릿수)
        # 'result4':f'{num1} / {num2} = {round(num1/num2,2)}',
        'result4':result4,
    }
    return render(request, 'myApp/sub9_result.html', context)  


# /myApp/sub10 주소와 연결되는 뷰함수
def sub10(request):
    return render(request, 'myApp/sub10.html')  

# /myApp/sub11 주소와 연결되는 뷰함수
def sub11(request):
    return render(request, 'myApp/sub11.html')  

# /myApp/sub12 주소와 연결되는 뷰함수
def sub12(request):
    return render(request, 'myApp/sub12.html')  


# /myApp/all 주소와 연결되는 뷰함수
# student 테이블 모델에서 전체 레코드를 저장하고
# 관련 html 문서에 전달
def all(request):
    # Student 테이블 모델 레코드 저장
    # select * from myApp_student; 결과를 저장
    student_list = Student.objects.all()
    # 딕셔너리 구조로 만들어서 html 문서에 전달
    context = {'student_list' : student_list}
    return render(request, 'myApp/all.html', context)  

# /myApp/학생아이디/detail 주소와 연결되는 뷰함수
def detail(request, id):
    # id에 해당하는 학생 레코드를 저장
    # 변수명 = Student.objects.get(필드명 = 값)
    student = Student.objects.get( id = id )
    # 딕셔너리 형태로 전달
    context = {'student' : student}
    return render(request, 'myApp/detail.html', context)


# /myApp/register 주소와 연결되는 뷰함수
def register(request):
    return render(request, 'myApp/register.html')  

# /myApp/registerCon 주소와 연결되는 뷰함수
# 학생 추가 폼에서 데이터를 전달받은 후
# student 테이블 모델에 레코드로 추가
# 학생 전체보기 페이지로 이동
def registerCon(request):
    # POST 방식으로 전달받은 데이터를 변수에 저장
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']


    # DB에 레코드로 저장
    # 인스턴스변수 = 테이블 모델명(필드 = 값....)
    # 인스턴스변수.save()
    student = Student(s_name = name, s_major = major, s_age = age, s_grade = grade, s_gender = gender)
    student.save()
    
    return redirect('/myApp/all/')


# /myApp/학생아이디/wipe/ 주소와 연결되는 뷰함수
# 학생 레코드 삭제 
def wipe(request, id):
    # id 에 해당하는 학생 레코드를 저장 
    # 변수명 = Student.objects.get(필드명=값)
    # select * from myApp_student where id=학생아이디;
    student = Student.objects.get(id=id)
    
    # DB에서 레코드 삭제 
    student.delete() 

    # 학생전체보기 페이지로 이동 
    return redirect('/myApp/all/')
    
# /myApp/학생아이디/modify/ 주소와 연결되는 뷰함수
# 학생 수정
def modify(request, id):
    # id에 해당하는 학생 레코드를 저장
    # 변수명 = Student.objects.get(필드명 = 값)
    student = Student.objects.get( id = id )
    # 딕셔너리 형태로 전달
    context = {'student' : student}
    return render(request, 'myApp/modify.html', context)


# /myApp/modifyCon 주소와 연결되는 뷰함수
# 학생 수정 폼에서 데이터를 전달받은 후
# student 테이블 모델에 id와 동일한 레코드에 수정 반영
# 학생 전체보기 페이지로 이동
def modifyCon(request):
    # POST 방식으로 전달받은 데이터를 변수에 저장
    id = request.POST['id']
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']

    # id에 해당하는 학생 레코드를 저장
    student = Student.objects.get(id=id)


    # DB에 레코드로 저장
    # 인스턴스변수 = 테이블 모델명(필드 = 값....)
    # 인스턴스변수.save()
    #student = Student(s_name = name, s_major = major, s_age = age, s_grade = grade, s_gender = gender)
    #student.save()


    # 데이터 업데이트
    student.s_name = name
    student.s_major = major
    student.s_age = age
    student.s_grade = grade
    student.s_gender = gender
    
    student.save()

    # 학생전체보기 페이지로 이동
    return redirect('/myApp/all/')


# /myApp/city 주소와 연결되는 뷰함수
# city 테이블 모델에서 전체 레코드를 저장하고
# 관련 html 문서에 전달
def city(request):
    # 테이블모델명.objects.all()
    city_list = City.objects.all()
    #return HttpResponse(city_list)
    # 딕셔너리 구조로 만들어서 html 문서에 전달
    context = {'city_list' : city_list}
    return render(request, 'myApp/city.html', context)

