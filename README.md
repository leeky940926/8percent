# 원티드x위코드 백엔드 프리온보딩 과제4 :: 8퍼센트(eightpercent)

# 배포 주소 : 

### 1. [TEAM] WithCODE

#### Members

| 이름   | github                         |
| ------ | ------------------------------ |
| 김민호 | https://github.com/maxkmh712   |
| 김주형 | https://github.com/BnDC        |
| 박치훈 | https://github.com/chihunmanse |
| 박현우 | https://github.com/Pagnim      |
| 이기용 | https://github.com/leeky940926 |
| 이정아 | https://github.com/wjddk97     |

-----

### 2. 과제

#### [필수 포함 사항]

- READ.ME 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

#### [과제  안내]

- 8퍼센트 기술스택: Python Django ( 백엔드를 100% Python + Django 으 로 쌓아올린 첫번째 금융회사입니다. )

#### 📝 다음과 같은 내용을 포함하는 테이블을 설계하고 다음과 같은 기능을 제공하는 REST API 서버를 개발해주세요.

#### 1. REST API 기능

- 거래내역 조회 API
- 입금 API
- 출금 API

#### 2. 개발 조건

2-1. 고려사항
- 계좌의 잔액을 별도로 관리해야 하며, 계좌의 잔액과 거래내역의 잔액의 무결성의 보장
- DB를 설계 할때 각 칼럼의 타입과 제약

2-2. 구현 안해도 되는 부분
- 문제와 관련되지 않은 부가적인 정보. 예를 들어 사용자 테이블의 이메일, 주소, 성별 등
- 프론트앤드 관련 부분

2-3. 제약사항
-(8퍼센트가 직접 로컬에서 실행하여 테스트를 원하는 경우를 위해) 테스트의 편의성을 위해 mysql, postgresql 대신 sqllite를 사용해 주세요.


-----

### 3. Skill & Tools

- **Skill :** <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"/>
- **Depoly :** <img src="https://img.shields.io/badge/AWS EC2-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/AWS RDS-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"/> <br>
- **ETC :**  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

-----

### 

-----

### 4. 모델링

![image](https://user-images.githubusercontent.com/75020336/141411964-a32b7190-5430-4eb3-b34f-f5b4c2bd8de6.png)

-----

### 5. Postman API 테스트

### API 테스트 : https://documenter.getpostman.com/view/17715735/UVC8B5hr

-----

### 6. 구현 사항 상세 설명

### POST /users/signin (로그인)

이메일과 비밀번호를 입력받아 jwt로 변환한 유저 토큰값을 반환해줍니다.

만약 이메일과 비밀번호 중 하나라도 일치하지 않으면 401 code를 return 해줍니다.

받아오는 key 값이 일치하지 않을 시 400 code를 return 해줍니다.

### POST /deals (입 출금)

deal_position 테이블을 따로 분리해 입금은 id=1, 출금은 id=2로 구분 하여 한 url안에서
입출금이 둘 다 구현되도록 하였습니다.

description을 만들어서 적요를 표현하였습니다.

돈을 입금하거나 출금시 거래 시간, 입금 금액, 잔여 금액, 적요, 입출금, 계좌를 거래 내역에 추가하였습니다.

잔여 금액보다 더 많은 금액을 출금할 시 400 code를 return 해줍니다.

받아오는 key 값이 일치하지 않을 시 400 code를 return 해줍니다.

-----

### 7. Unittest 결과

Unittest는 제공되는 test case를 기반으로 작성하였으며 그 외 요청 실패 사례들을 추가하였습니다.

>### 로그인 유닛테스트
![image](https://user-images.githubusercontent.com/75020336/141413507-dfe89234-cb7d-4226-be45-4c04b08ade15.png)

-----

### 8. Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 원티드랩(wantedlab)에서 출제한 과제를 기반으로 만들었습니다.

0. 시나리오
: 박현우("hyeon7200@naver.com")는 오늘 월급일 및 카드대금결제일이며, 입/출금이 잘 이루어졌는지 로그인해서 확인 해보려고 함
입/출금은 구현된 API를 통해 거래내역에 추가되며, 마지막 시나리오에서 조회 예정

박현우("hyeon7200@naver.com")는 팡팡은행(banks.id=5)과 나무은행(banks.id=6)에 계좌가 존재하며, 
이번 테스트를 위해 만든 농협 계좌에서 입출금을 진행할 예정
팡팡은행에는 현재 1,000,000원의 잔액(accounts.balance)을 최초로 입금해놓은 상태이며,
거래내역 조회는 팡팡은행의 경우, 생성된지 얼마 안된 계좌기 때문에 내역이 존재하지 않아 나무은행 계좌로 진행할 예정


1. 로그인

1-1. 아이디 오입력
이메일을 잘못 기억하고 있어서 "hyoen4@naver.com.com"로 입력 후 로그인 시도
(email : "hyoen4@naver.com@8percent.com", password="test"로 request.body 작성해서 테스트) 

1-2. 비밀번호 오입력
비밀번호를 빠르게 입력하려다가 실수로 잘못된 비밀번호를 입력 후 로그인 시도
(email : "hyeon7200@naver.com", password="test"로 request.body 작성해서 테스트)

1-3. 로그인 성공
이메일과 비밀번호를 올바르게 입력해서 로그인에 성공했으며, 토큰까지 발급 완료
(email : "hyeon7200@naver.com", password="1234" 입력 후 토큰 발급 받은 것까지 request.body에 작성해서 테스트)


2. 입금/출금

2-1. 입금
매월 12일은 월급날이며, 세후 수령액은 2,800,000원이다. 2,800,000을 계좌에 입금해줍니다.

2-2. 출금
매월 12일은 카드대금결제일이며, 이번 달 결제액은 800,000원이다. 800,000을 계좌체서 출금해.

2-3. 잔액초과금액 출금
현재 계좌에는 3,000,000원이 남아있는 상태이며, 4,000,000원 상당의 컴퓨터를 할부로 구매해야 되는데, 직원이 실수로 일시불결제를 누름
이 때, 계좌잔액의 초과금액을 결제 요청한것이기 때문에 "CANNOT_REQUEST_EXCEED_BALANCE"라는 문구와 함께 에러코드는 400을 리턴


3. 거래내역 조회

3-1. 입/출금 구분에 따른 조회

박현우는 이번 달에 월급외에 추가적으로 들어오는 부수입이 있는지 확인하고자, 순수 지출내역은 얼마인지 확인하고자 입/출금 내역에 따른 조회를 하려고 함
(입금일 때, 출금일 때 데이터 셋 조회)

3-2. 거래일시에 따른 조회

박현우는 한달동안 친구의 결혼식이 두 번 있었기 때문에 축의금으로 꽤 지출한 돈이 많아서, 최근 1달 기준 거래내역을 조회해서 이번 달 마진이 얼만지 확인해보려고 함
(최근 1달 거래내역 가져옴 및 페이지네이션)
