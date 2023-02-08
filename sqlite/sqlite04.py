# DB안의 테이블안에 레코드 삽입 

# 1) 관련 임포트 
import sqlite3

# 2) 데이타베이스 연결 
# 연결변수 생성 
# 연결변수명 = sqlite3.connect(데이타베이스경로)
# bookDb.db 파일이 없다면 새로 생성 . 
# 파일 있다면 연결.
conn = sqlite3.connect('bookDb.db')
print('\n\n 데이타베이스 연결 완료')

# 3) 작업변수 생성 
# 작업변수명 = 연결변수.cursor() 
cursor = conn.cursor()

# 4) 전체 레코드수 확인 


"""
cursor.execute('select * from book1')
result = cursor.fetchall()
print('전체 레코드수는? ', len(result))
print('='*50)
for row in result:
    print(row)
print('='*50)
"""


# 5) 레코드 삭제 + 확인  (1)
# 작업변수.execute(sql명령어-레코드 삭제)
# 연결변수.commit()

"""
cursor.execute('delete from book1 where id = 1')
conn.commit()

cursor.execute('select * from book1')
result = cursor.fetchall()
print('삭제 후의 전체 레코드수는? ', len(result))
"""

# 5) 레코드 삭제 + 확인  (2)
# sql명령어변수 = sql명령어-레코드삭제
# 작업변수.execute(sql명령어변수, (값1, 값2 ... ))
# 연결변수.commit()

"""
sql = 'delete from book1 where writer = ?;'
cursor.execute(sql, ('조앤 K. 롤링',))
conn.commit()

cursor.execute('select * from book1')
result = cursor.fetchall()
print('삭제 후의 전체 레코드수는? ', len(result))
print('='*50)
for row in result:
    print(row)
print('='*50)
"""

# 5) 다중 for문을 이용한 출력 양식 변경
# 아이디 => ?
# 책 제목 => ?
# 저자 => ?
# 페이지수 => ?
# 가격 => ?

cursor.execute('select * from book1 order by id desc limit 5')
result = cursor.fetchall()
#print(result)
print('='*50)
for row in result:
    # for item in row:
    #     print('아이디', item)
    for row in range(5):
        print(title_list[i], '=>',  row[i])
    print('_'*50)
# 마지막 단계 - DB 반환
conn.close()