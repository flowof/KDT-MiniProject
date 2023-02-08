# 다음과 같이 sqlite를 이용하여 주소록 프로그램을 완성하여라. 
# quiz_connect_수강생명.py 으로
# coderecipe@naver.com으로 제출
'''


==================================================
    주소록 메뉴
==================================================

1. 연락처 입력
2. 연락처 출력
3. 연락처 수정
4. 연락처 삭제
5. 연락처초기화
6. 종료

# 연락처 수정 예시  

수정 레코드 코드 => ? 

1. 이름   2. 핸드폰   3. 이메일   4. 주소 

수정 메뉴 선택 => ?

레코드가 수정되었습니다. 


# 연락처 삭제 예시 

수정 레코드 코드 => ? 

해당 레코드가 삭제되었습니다.



'''


# sqlite 임포트 
import sqlite3

# 연결변수와 작업변수 생성
conn = sqlite3.connect('contact2.db')
cursor = conn.cursor() 

# 테이블 생성 함수 정의 
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contactTbl (
            code integer not null primary key autoincrement, 
            name text not null, 
            mobile text not null, 
            email text, 
            addr text not null
        );
    ''') 
    conn.commit()

# 레코드 삽입 함수 정의 
def insert_record():
    print('='*50)
    print('\t 레코드 삽입')
    name = input('이름 : ')
    mobile = input('핸드폰 : ')
    email = input('이메일 : ')
    addr = input('주소 : ')

    sql = 'INSERT INTO contactTbl (name, mobile, email, addr) VALUES (?, ?, ?, ?);'
    cursor.execute(sql, (name, mobile, email, addr))
    conn.commit()


# 레코드 출력 함수 정의 
def print_record():
    sql = 'SELECT * FROM contactTbl;'
    cursor.execute(sql)
    result = cursor.fetchall()
    # 주소록에 데이타가 없다면 메세지 출력. 
    if len(result) == 0:
        print('등록된 주소 목록이 없습니다.')
    else:
        print('-'*50)
        print(' 번호   이름          핸드폰         이메일        주소')
        print('_'*50)
        for row in result:
            for item in row:
                print(' ', item, end='   ')
            print('\n')


# 레코드 전체 삭제 => 초기화 
def delete_all():
    sql = 'DELETE FROM contactTbl'
    cursor.execute(sql)
    conn.commit() 
    print('레코드가 모두 삭제되었습니다.')



# 함수 호출 => 테스트용 
create_table() 
# insert_record()
# insert_record()
# print_record()
# delete_all()
# print_record()


# 메인 메뉴 기능 
# while True:
#     print()
#     print('='*50)
#     print('    주소록 메뉴')
#     print('='*50)
#     print('')
#     print('1. 연락처 입력')
#     print('2. 연락처 출력')
#     print('3. 연락처 수정')
#     print('4. 연락처 삭제')
#     print('5. 연락처초기화') 
#     print('6. 종료')
#     print('='*50)
#     print() 
#     menu = input('메뉴선택: ')
#     if menu == '1':
#         insert_record()
#     elif menu == '2':
#         print_record()
#     elif menu == '3':
#         pass
#     elif menu == '4':
#         pass
#     elif menu == '5':
#         delete_all()
#     elif menu == '6':
#         print('프로그램 종료')
#         break  
#     else:
#         print('잘못된 입력입니다. 다시 입력하세요')

# 데이타베이스 종료 
conn.close()


