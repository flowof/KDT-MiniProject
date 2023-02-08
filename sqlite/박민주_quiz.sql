-- 박민주_quiz

-- 1) userTBL 테이블을 다음과 같은 구조로 생성한 후 구조를 확인한다.
/*
  userID  	TEXT NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  userName  TEXT NOT NULL, -- 이름
  birthYear 	INTEGER NOT NULL,  -- 출생년도
  addr	  	TEXT NOT NULL, -- 지역
  mobile1	TEXT, -- 휴대폰의 국번(010, 011, 016, 017, 018, 019 등)
  mobile2	TEXT, -- 휴대폰의 나머지 전화번호(하이픈제외)
  height    	INTEGER,  -- 키
  mDate    	date  -- 회원 가입일

 
 CREATE TABLE userTBL(
  userID  	TEXT NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  userName  TEXT NOT NULL, -- 이름
  birthYear INTEGER NOT NULL,  -- 출생년도
  addr	  	TEXT NOT NULL, -- 지역
  mobile1	TEXT, -- 휴대폰의 국번(010, 011, 016, 017, 018, 019 등)
  mobile2	TEXT, -- 휴대폰의 나머지 전화번호(하이픈제외)
  height    INTEGER,  -- 키
  mDate    	date  -- 회원 가입일
 );
  */



-- 2) userTBL에 아래  데이터를 참조하여 데이터를 삽입하고 출력하여라.
/*
USERID   USERNAME    BIRTHYEAR      ADDR      MOBILE1    MOBILE2    HEIGHT       MDATE   
--------    ----------           ---------- -- --- -------- ---------- -       -------
LSG         이승기           1987                  서울          011   11111111          182       08/08/08
KBS         김범수           1979                  경남          011   22222222          173      12/04/04
KKH        김경호           1971                  전남          019   33333333          177       07/07/07
JYP         조용필           1950                  경기          011    44444444         166       09/04/04
SSK         성시경           1979                  서울                                             186      13/12/12
LJB          임재범           1963                  서울          016     66666666        182        09/09/09
YJS         윤종신           1969                  경남                                             170        05/05/05


INSERT INTO userTBL VALUES ("LSG", "이승기", 1987, "서울", "011", "11111111", 182, "2008-08-08");
INSERT INTO userTBL VALUES("KBS", "김범수", 1979, "경남", "011", "22222222", 173, "2012-4-4");
INSERT INTO userTBL VALUES("KKH", "김경호", 1971, "전남", "019", "33333333", 177, "2007-7-7");
INSERT INTO userTBL VALUES("JYP", "조용필", 1950, "경기", "011", "44444444", 166, "2009-4-4");
INSERT INTO userTBL VALUES("SSK", "성시경", 1979, "서울", NULL  , NULL      , 186, "2013-12-12");
INSERT INTO userTBL VALUES("LJB", "임재범", 1963, "서울", "016", "66666666", 182, "2009-9-9");
INSERT INTO userTBL VALUES("YJS", "윤종신", 1969, "경남", NULL  , NULL      , 170, "2005-5-5");
*/



-- 3) userTBL 테이블에서 ADDR 컬럼값이 경남인 경우 경남을 부산으로 데이터값을 수정하여라.

/*
 SELECT * from userTBL;
UPDATE userTBL
	SET addr = "부산"
	WHERE addr ="경남";
*/



-- 4) userTBL 테이블에서 MOBILE1과 MOBILE2 값이 NULL 인 경우
--    011, 55555555 값으로 수정하여라.

/*
SELECT mobile1, mobile2 FROM userTBL;

UPDATE userTBL
	SET mobile1 = "011", mobile2 = "55555555"
	WHERE mobile1 ISNULL;

SELECT * FROM userTBL;
*/



-- 5) userTBL 테이블 모두를 복사하여 userTBL2 테이블로 생성하여라. 

/*
CREATE TABLE userTBL2 as SELECT * FROM userTBL;
*/



-- 6) userTBL2 테이블에서 국번이 011인 데이터를 삭제하여라.
/*
SELECT * FROM userTBL2;
DELETE FROM userTBL2 WHERE mobile1="011";
*/

	

-- 8) userTBL 테이블에서 지역이 서울, 경기인 레코드만 복사하여 userTBL3 테이블로 생성하여라.  

/*
CREATE TABLE userTBL4 
	as SELECT * FROM userTBL
	WHERE (addr = "서울") or (addr = "경기");
	
DROP TABLE userTBL3;

ALTER TABLE userTBL4 RENAME to userTBL3;



CREATE TABLE userTBL3 
	as SELECT * FROM userTBL
	WHERE (addr = "서울") or (addr = "경기");
*/



-- 9) userTBL3 테이블에서 BIRTHYEAR 컬럼명을 BIRTH로 변경하여라.

/*
ALTER TABLE userTBL3 RENAME birthYear TO BIRTH;

SELECT * FROM userTBL3;
*/



-- 10) userTBL3 테이블에서 AGE 컬럼을 추가하고 현재년도와 BIRTH 컬럼을 이용하여 데이터를 수정하여라.
/*
ALTER TABLE userTBL3 ADD COLUMN age INTEGER;

SELECT * FROM userTBL3;

*/

--UPDATE TABLE userTBL3 set age = (sysyear - BIRTH + 1);
-- SELECT sysdate FROM userTBL3;
--UPDATE userTBL3 SET AGE= 14 WHERE BIRTH="1950" OR mDate="2008-08-08";
-- UPDATE TABLE userTBL3 set age = ("2021" - BIRTH + 1);



-- 11) userTBL3 테이블에서  MDATE와 height 컬럼을 삭제하여라.
-- sqlite에서는 DROP COLUMN 명령문이 없다.
-- ALTER TABLE userTBL3 DROP COLUMN MDATE; -- 안된다. 
-- 공식 사이트에서는 DROP TABLE, ALTER TABLE RENAME TO문을 이용하라고 가이드 하고 있다.
DROP COLUMN mDate;
-- SELECT * FROM userTBL3;

