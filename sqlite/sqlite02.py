# sqlite + python 연동

# 1) 관련 임포트
import sqlite3

# 데이터베이스 연결
# 연결변수 생성
# 연결변수명 = sqlite3.connect(데이터베이스경로)
# bookDb.db 파일이 없다면 새로 생성.
# 파일 있다면 연결.
conn = sqlite3.connect('bookDb.db')
print('데이터베이스 연결 완료')

# 3) 작업변수 생성
# 작업변수명 = 연결변수.cursor()
cursor = conn.cursor()

# 4) 레코드 삽입 sql 명령 실행 후 데이터베이스 반영 +확인 (1)
# 작업변수.execute(sql명령어-레코드삽입)
# 연결변수.commit()

"""
cursor.execute('''
                insert into book1
                    values(null, '파이썬완성', '홍길동', 300, 35000);
''')

conn.commit();
"""

"""
#레코드 조회
cursor.execute('select * from book1')
result = cursor.fetchall() # 리스트 안의 튜플
print(result) #[]
print('='*30)
for row in result:
    print(row)
"""

# 4) 레코드 삽입 sql 명령 실행 후 데이터베이스 반영 1 + 확인 (2)
# 작업변수.execute(sql명령어-레코드삽입)
# 연결변수.commit()
"""
cursor.execute('''
                insert into book1 (title, writer, page, price)
                    values('장고로 웹사이트 제작', '김장고', 400, 40000);
''')

conn.commit();


# 레코드 조회
cursor.execute('select * from book1 order by id desc')
result = cursor.fetchall() #리스트 안의 튜플
print('='*30)
for row in result:
    print(row)
"""

# 4) 레코드 삽입 sql 명령 실행 후 데이터베이스 반영 + 확인 (3)
# 컬럼명 + ? 이용
# 작업변수.execute(sql명령변수, (값1, 값2, ...))
# 연결변수.commit()
"""
sql = "insert into book1 (title, writer, page, price) values (?, ?, ?, ?);"

cursor.execute(sql, ('머신러닝 라이브러리', '최머신', 600, 56000))
conn.commit();

#레코드 조회 - 역순으로 정렬해서 3개의 레코드만 저장
cursor.execute('select * from book1 order by id desc limit 3')
result = cursor.fetchall() #리스트 안의 튜플
print('='*30)
for row in result:
    print(row)
"""

# 4) 레코드 삽입 sql 명령 실행 후 데이터베이스 반영 + 확인 (4)
# ? + executemany() 를 이용한 다중 데이터 삽입

#sql 명령변수 = "insert into 테이블명 (zjffjaaud1, ....) values (?, ? ...);"
# 리스트명 = [(값1, 값2....), (값1, 값2....), (값1, 값2....)...]
# 작업변수.executemany(sql명령변수, 리스트명)
# 연결변수.commit()

sql = "insert into book1 (title, writer, page, price) values (?, ?, ?, ?);"
data_list = [('해리포더1', '조앤 K. 롤링', 500, 25000),
             ('해리포더2', '조앤 K. 롤링', 500, 25000),
             ('해리포더3', '조앤 K. 롤링', 500, 25000)
             ]
cursor.executemany(sql, data_list)
conn.commit();

#레코드 조회
cursor.execute('select * from book1 order by id desc')
result = cursor.fetchall() # 리스트 안의 튜플
print('='*30)
for row in result:
    print(row)


# 데이터베이스 종료
conn.close()