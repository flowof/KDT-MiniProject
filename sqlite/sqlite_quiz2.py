# 다음과 같이 sqlite를 이용하여 주소록 프로그램을 완성하여라. 
# quiz_connect_수강생명.py 으로
# coderecipe@naver.com으로 제출
'''
# 첫번째 화면

1. 연락처 입력
2. 연락처 출력
3. 연락처 삭제
4. 연락처초기화
5. 종료

메뉴선택: 1


# 두번째 화면 
# 연락처 입력

Name: ?
Phone Number: ?
E-mail: ?
Address: ?

# 모두 입력하였다면 
# 세번째 화면으로 이동 

1. 연락처 입력 
2. 연락처 출력 
3. 연락처 삭제 
4. 연락처초기화
5. 종료   

메뉴선택: 2

# 2번 선택시 
# 네번째 연락처 출력 화면 
# 레코드 모두 출력

(1, '홍길동', '010676898', 'gogo@naver.com', '부산 금정구')

# 레코드 모두 출력 후에
# 메인 메뉴 화면으로 이동

1. 연락처 입력
2. 연락처 출력
3. 연락처 삭제
4. 연락처초기화
5. 종료

메뉴선택: 3

# 메인 메뉴에서 3번 입력시
# 연락처 삭제 화면으로 이동
# Name 값 입력

Name: 홍길동
data delete

# 레코드 삭제 후 
# 메인 메뉴 화면으로 이동

1. 연락처 입력
2. 연락처 출력
3. 연락처 삭제
4. 연락처초기화
5. 종료

메뉴선택: 2

# 2번 입력 후 연락처 출력 화면으로 이동
# 만약 레코드가 없다면 메세지 출력 후
# 메인 메뉴 이동

contact is empty
1. 연락처 입력
2. 연락처 출력
3. 연락처 삭제
4. 연락처초기화
5. 종료

메뉴선택: 5

# 메인 메뉴에서 5번을 입력하면
# 프로그램 종료

# 메인 메뉴에서 연락처 초기화
# 4 입력시
# 레코드 모두 삭제


'''
# sqlite 임포트 
from os import name
import sqlite3
#from sqlite3.dbapi2 import Cursor


conn = sqlite3.connect('contact2.db')
Cursor = conn.cursor()

# 테이블 생성 함수 정의
def create_table():
    Cursor.execute('''
        create table if not exists contactTbl(
           code integer not null primary key autoincrement,
           name text not null,
           mobile text not null,
           email text,
           addr text not null
        );
    ''')
    conn.commit()

# 함수 호출
create_table()

# 데이터베이스 종료
#conn.close()
    


# 레코드 삽입 함수 정의
def insert_record():
    print('='*50)
    print('\t 레코드 삽입')
    name = input('Name : ')
    mobile = input('핸드폰 : ')
    email = input('이메일 : ')
    addr = input('주소 : ')
    sql = 'insert into contactTbl (name, mobile, email, addr) values (?, ?, ?, ?);'
    Cursor.execute(sql, (name, mobile, email, addr))
    conn.commit()

# 레코드 출력 함수 정의
def print_record():
    sql = 'select * from contactTbl;'
    Cursor.execute(sql)
    result = Cursor.fetchall()
    # 주소록에 데이터가 없다면 메시지 출력.
    if len(result) == 0:
        print('등록된 주소가 없습니다.')
    else:
        print('-'*50)
        print('이름           핸드폰         이메일        주소')
        print('_'*50)
        for row in result:
            for item in row:
                print(item, end='   ')
        print('\n') 

# 레코드 전체 삭제 => 초기화
def delete_all():
    sql = 'delete from contactTbl'
    Cursor.execute(sql)
    conn.commit()
    print('레코드가 모두 삭제되었습니다.')

# 함수 호출
"""
create_table()
insert_record()
insert_record()
print_record()
"""

"""
delete_all()
print_record()
"""


# 메인메뉴 기능
while True:
    print()
    print('='*50)
    print('     주소록 메뉴')
    print('='*50)
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 수정')
    print('4. 연락처 삭제')
    print('5. 연락처초기화')
    print('6. 종료')
    print('='*50)
    print()
    menu = input('메뉴선택: ')
    if menu == '1':
        insert_record()
    elif menu == '2':
        print_record()
    elif menu == '3':
        pass
    elif menu == '4':
        pass
    elif menu == '5':
        pass
    elif menu == '6':
        print('프로그램 종료')
        break
    else:
        print('잘못된 입력입니다. 다시 입력하세요')



# 데이터베이스 종료
conn.close()    

