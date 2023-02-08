# sqlite + python 연동

# 1) 관련 임포트
import sqlite3

# 데이터베이스 연결
# 연결변수 생성
# 연결변수명 = sqlite3.connect(데이터베이스경로)
# bookDb.db 파일이 없다면 새로 생성.
# 파일 있다면 연결.
conn = sqlite3.connect('bookDb.db')

# 3) 작업변수 생성
# 작업변수명 = 연결변수.cursor()
cursor = conn.cursor()
print(cursor, type(cursor))

# 4) sql 명령 실행
# 테이블 생성 => bookDb.db > book
# create table 테이블명 (필드명 자료형 옵션);
# 작업변수.execute(sql명령어)

#테이블이 없다면 새로 생성.
cursor.execute('''
            create table if not exists book1 (
                id integer not null primary key autoincrement,
                title text not null,
                writer text,
                page integer,
                price integer
            );
''')
print("table 생성완료")
# 5) db에 반영
# 연결변수.commit()
conn.commit

# 6) 테이블 안의 레코드 출력
# 작업변수.execute(sql 명령어 중에서 select)
# 결과저장변수 = 작업변수.fetchall()
# 결과저장변수 = 작업변수.fetchone()
# 결과저장변수 = 작업변수.fetchmany(갯수)

cursor.execute('select * from book1')
result = cursor.fetchall()
print(result)






# 데이터베이스 종료
conn.close()
