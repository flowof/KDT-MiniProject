-- 특정 테이블의 전체 레코드 확인
-- SELECT * FROM 테이블명

-- SELECT * FROM artists;
-- 
-- SELECT * FROM employees;

-- 특정 테이블의 특정 컬럼의 레코드 확인
-- SELECT 필드명1, 필드명2... FROM 테이블명

-- SELECT EmployeeId, LastName, FirstName FROM employees;

-- 특정 테이블에서 레코드수 제한하여 출력하기
-- SELECT * FROM 테이블명 LIMIT 숫자;
-- SELECT 필드명1, 필드명2 FROM 테이블명 LIMIT 숫자;

-- CUSTOMERS 테이블에서 5개의 레코드 보기
-- SELECT * FROM customers LIMIT 5;

-- 전체 레코드 갯수 
-- SELECT count(*) FROM customers; -- 59 
-- 
-- SELECT CustomerId, City FROM customers LIMIT 5;


-- WHERE 조건절
--  = , <=, >=, <, > 비교연산자
--   AND, OR, NOT 논리연산자 

-- SELECT 필드명 FROM 테이블명 WHERE 조건절 ;

-- customers 테이블에서 CustomerId 가 10인 레코드 보기

-- SELECT * 
-- 		FROM customers
-- 		WHERE customerId = 10;
		
-- customers 테이블에서 CustomerId 가 10 이거나 30 인 레코드 보기		
		
-- SELECT * 
-- 		FROM customers
-- 		WHERE customerId = 10 OR customerId = 30;		
		
-- PLAYLISTS 테이블에서 PlaylistId가 5보다 큰 레코드 보기
-- SELECT * 
-- 	FROM playlists
-- 	WHERE playlistId > 5;		

	
-- PLAYLISTS 테이블에서 PlaylistId가 5보다 크고 10보다 작은 레코드 보기
SELECT * 
	FROM playlists
	WHERE (playlistId > 5) AND (PlaylistId < 10);		
 		

	
		
		