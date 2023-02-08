# DB 안의 테이블 안에 레코드 삽입

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

# 4) 값 수정 + 확인 (1)
# 작업변수.execute(sql명령어-레코드수정)
# 연결변수.commit()


"""
cursor.execute('update book1 set price=10000 where id=2;')
conn.commit();

#레코드 조회
cursor.execute('select * from book1 where id=2')
result = cursor.fetchone() # 튜플
#result = cursor.fetchall() # 리스트 안의 튜플
print(result)

"""

# 4) 값 수정 + 확인 (2) - ? 이용
# sql 변수명 =?를 이용한 update 명령 => update 테이블명 set 컬럼명=? where 컬럼명=?;
# 작업변수.execute(sql변수, (값1, 값2))
# 연결변수.commit()

sql = 'update book1 set price=? where writer = ?;'
cursor.execute(sql, (12000, '홍길동'))
conn.commit();

# 레코드 조회
sql2 = 'select * from book1 where writer =?;'
#(값1, 값2)다중튜플
# 튜플원소가 하나인 경우는 (값,) ,가 없으면 문자열로 들어감
cursor.execute(sql2, ('홍길동',))
result = cursor.fetchone() # 튜플
#result = cursor.fetchall() # 리스트 안의 튜플
print(result)

#마지막 단계
conn.close()