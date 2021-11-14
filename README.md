# 원티드x위코드 백엔드 프리온보딩 과제4 :: 8퍼센트(eightpercent)

# 배포 주소 : 3.143.233.195:8000

# 1. [TEAM] WithCODE 소개 및 본인 소개

#### Members

| 이름   | github                         |
| ------ | ------------------------------ |
| 김민호 | https://github.com/maxkmh712   |
| 김주형 | https://github.com/BnDC        |
| 박치훈 | https://github.com/chihunmanse |
| 박현우 | https://github.com/Pagnim      |
| 이기용 | https://github.com/leeky940926 |
| 이정아 | https://github.com/wjddk97     |


#### 본인소개

안녕하세요.

위코드x원티드 백엔드 프리온보딩과정 교육생 이기용입니다.

해당 Git Repository는 11월 11일 ~ 11월 13일까지 8percent 기업과제 내용이 담겨져 있습니다.

최초의 Git Repository링크는 https://github.com/maxkmh712/8percent.git 이며,

제 Repository로 Fork를 했습니다.

이번 과제에서 저는 3가지 역할을 맡았습니다.

1. 입/출금API 구현 및 Unit Test
2. VACUUM을 이용한 sqlite 용량 최적화 방안 제시
3. Functional Test를 위한 시나리오 작성

아래엔 구현 내용에 대한 상세설명이 작성되어 있습니다.

읽어주셔서 감사합니다.

------



# 2. 과제

#### [필수 포함 사항]

- READ.ME 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

#### [과제 안내]

- 8퍼센트 기술스택: Python Django ( 백엔드를 100% Python + Django 으로 쌓아올린 첫번째 금융회사입니다. - 채용공고 中)

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

- (8퍼센트가 직접 로컬에서 실행하여 테스트를 원하는 경우를 위해) 테스트의 편의성을 위해 mysql, postgresql 대신 sqllite를 사용해 주세요.

------

# 3. Skill & Tools

- **Skill :** [![img](https://camo.githubusercontent.com/0f3eb5f3e4c61d94657f16605ea420a0216673dfb085d100c458ed15be0599d2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/0f3eb5f3e4c61d94657f16605ea420a0216673dfb085d100c458ed15be0599d2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/c4c1014e1f168ff271282b67ec9059c3cfc16b2a5cba6e0c7c98c3530f47f45c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/c4c1014e1f168ff271282b67ec9059c3cfc16b2a5cba6e0c7c98c3530f47f45c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/9bf3ab62e0f872ed37f7d590e4577137b2dda11ffb0786f9b858cd39c2dc8c7f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d23303033423537)](https://camo.githubusercontent.com/9bf3ab62e0f872ed37f7d590e4577137b2dda11ffb0786f9b858cd39c2dc8c7f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d23303033423537)
- **Depoly :** [![img](https://camo.githubusercontent.com/9ad32f291fa1163a77cd2e919f8378b38bf66fd9de517178bf890e521178f341/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f415753204543322d3233324633453f7374796c653d666f722d7468652d6261646765266c6f676f3d416d617a6f6e20415753266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/9ad32f291fa1163a77cd2e919f8378b38bf66fd9de517178bf890e521178f341/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f415753204543322d3233324633453f7374796c653d666f722d7468652d6261646765266c6f676f3d416d617a6f6e20415753266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/fbef20533fc559c07dcaae57d63beab86709421dfd5428391a563096c88ead5a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3234393645443f7374796c653d666f722d7468652d6261646765266c6f676f3d446f636b6572266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/fbef20533fc559c07dcaae57d63beab86709421dfd5428391a563096c88ead5a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3234393645443f7374796c653d666f722d7468652d6261646765266c6f676f3d446f636b6572266c6f676f436f6c6f723d7768697465)
- **ETC :** [![img](https://camo.githubusercontent.com/fdb91eb7d32ba58701c8e564694cbe60e706378baefa180dbb96e2c1cfb9ec0f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d476974266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/fdb91eb7d32ba58701c8e564694cbe60e706378baefa180dbb96e2c1cfb9ec0f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d476974266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/23a917c56e310800a66c58a03447dd42c0dea2abff415ef9719e3e837c1cff82/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/23a917c56e310800a66c58a03447dd42c0dea2abff415ef9719e3e837c1cff82/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/879423585ed087f3c973857c43ba7e7d84f52c993d2c937055726339fbf921d9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d506f73746d616e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/879423585ed087f3c973857c43ba7e7d84f52c993d2c937055726339fbf921d9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d506f73746d616e266c6f676f436f6c6f723d7768697465)

------

# 4. 모델링

[![8persent (1)](https://user-images.githubusercontent.com/61782539/141447955-25afbac0-808d-457e-812d-83b4376d9d90.png)](https://user-images.githubusercontent.com/61782539/141447955-25afbac0-808d-457e-812d-83b4376d9d90.png)

------

# 5. Postman API 테스트

### API 테스트 : https://www.postman.com/cloudy-resonance-766003/workspace/8percent/collection/17715735-79c01c1b-885b-48f9-a9a2-1b9b12a24055

기본 주소는 배포주소로 되어 있으며, 콜렉션 fork 후 테스트 부탁드립니다.

### API 명세서 : https://documenter.getpostman.com/view/17715735/UVC8B5hr

------

# 6. 구현 사항 상세 설명

### POST /users/signin (로그인)

이메일과 비밀번호를 입력받아 jwt로 변환한 유저 토큰값을 반환해줍니다.

만약 이메일이나 비밀번호가 올바르지 않을시 401 code를 return 해줍니다.

body의 key 값이 일치하지 않을 시 400 code를 return 해줍니다.

### POST /deals/int:account_id (입출금)

deal_position 테이블을 따로 분리해 입금은 id=1, 출금은 id=2로 구분 하여 하나의 API에서 입출금이 구현되도록 하였습니다.

path변수로 계좌 id를 식별하여 해당 계좌에 입출금 요청을 합니다. 해당 계좌가 존재하지 않을시 404 code를 return 합니다.

토큰의 user가 해당 계좌를 갖고 있는 user가 아닐시 400 code를 return 해줍니다.

돈을 입금하거나 출금시 거래 시간, 입출금 금액, 잔여 금액, 적요, 해당 계좌를 거래 내역에 추가하였습니다.

transaction을 적용하여 계좌의 잔액변동과 거래 내역의 생성이 일괄적으로 이루어지고, 계좌의 잔액과 거래 내역의 잔액 무결성이 유지되도록 하였습니다.

잔여 금액보다 더 많은 금액을 출금할 시 400 code를 return 해줍니다.

body의 key 값이 일치하지 않을 시 400 code를 return 해줍니다.

요청에 body가 존재하지 않을시 400 code를 return 합니다.

body에 들어온 deal_psotion_id가 잘못되었을 때 400 code를 return 합니다.

### GET /deals/int:account_id (계좌 거래내역 조회)

![](https://user-images.githubusercontent.com/61782539/141475824-d472f981-117c-4e8a-b678-616df1ec4484.png)

path변수로 계좌 id를 식별하여 해당 계좌의 거래내역을 조회합니다. 해당 계좌가 존재하지 않을시 404 code를 return 합니다.

토큰의 user가 해당 계좌를 갖고 있는 user가 아닐시 400 code를 return 해줍니다.

Query Parameter로 조회기간의 시작 날짜와 종료 날짜를 받아와서 해당 기간의 거래내역을 필터링합니다.

조회기간의 시작 날짜와 종료 날짜의 정보는 필수적이므로 해당 key들이 들어오지 않았을 때 400 code를 return 합니다.

잘못된 날짜 형식으로 들어왔을 때도 400 code를 return 합니다.

Query Parameter의 'sort' key로 최신순, 오래된순 정렬이 가능하도록 하였습니다. 만약 sort key가 들어오지 않거나 잘못된 Key로 들어왔을 때 기본 정렬은 최신순이 되도록 하였습니다.

'page' key로 page 데이터를 받아 Pagination이 가능하도록 하였습니다. 1page의 크기는 20으로 설정하였습니다. 만약 page key가 들어오지 않거나 잘못된 key로 들어왔을 때 기본 page는 1이 되도록 하였습니다.

'deal_positin_id' key로 입금내역만 조회하거나 출금내역만 조회할 수 있도록 필터링이 가능하도록 했습니다. 

잘못된 deal_position_id가 들어왔을 때 400 code를 return 합니다.

------

# 7. UnitTest 결과

[![스크린샷 2021-11-12 오후 6 56 58](https://user-images.githubusercontent.com/61782539/141448154-870549e2-ccf1-4328-ac35-794d84f516b8.png)](https://user-images.githubusercontent.com/61782539/141448154-870549e2-ccf1-4328-ac35-794d84f516b8.png)

------

# 8. Functional Test를 위한 시나리오 작성

시나리오별 예시는 상단에 기술한 Postman TEST url에서 TEST 할 수 있습니다.

- 시나리오 : 김민호([user1@8percent.com](mailto:user1@8percent.com))는 오늘 받은 월급을 계좌에 입금하고, 부모님 용돈을 출금 후에 입출금이 잘 이루어졌는지 거래내역을 확인 해보려고 함

1. 로그인

​    1-1. 아이디 오입력

​    이메일을 잘못 기억하고 있어서 "[hyoen4@naver.com.com](mailto:hyoen4@naver.com.com)"로 입력 후 로그인 시도

   1-2. 비밀번호 오입력

​    비밀번호를 빠르게 입력하려다가 실수로 잘못된 비밀번호를 입력 후 로그인 시도

   1-3. 로그인 성공

​    이메일과 비밀번호를 올바르게 입력해서 로그인에 성공했으며, 토큰까지 발급 완료

1. 입금/출금

   2-1. 입금

​    매월 12일은 월급날이며, 세후 수령액은 2,800,000원이다. 2,800,000을 계좌에 입금한다.

   2-2. 출금

   오늘 부모님 용돈을 드리기 위해서 800,000원을 출금한다.

   2-3. 잔액초과금액 출금

​    실수로 잔액보다 큰 금액을 출금 요청함.
​    이 때, 계좌잔액의 초과금액을 출금 요청한것이기 때문에 "INSUFFICIENT_BALANCE"라는 문구와 함께 에러코드는 400을 반환

1. 거래내역 조회

   3-1. 입/출금 구분에 따른 조회

​    김민호는 입출금이 잘 이루어졌는지 확인하고자 거래내역을 최신순으로 조회함

   3-2. 거래일시에 따른 조회

​    김민호는 10월 20일부터 1년 가량 계좌에서 출금한 금액이 얼마인지 계산해보고자 해당 기간의 출금 내역을 오래된순으로 조회함

# 9. 거래내역이 1억건이 넘어갈 경우를 대비한 설정

- #### **VACUUM**

테이블에 대량의 데이터가 쌓이면 허수 용량이 늘어날 수 있고, 최소 5년~최대 10년동안 고객의 거래내역을 저장하고 삭제할 수 있는 규정 상 테이블을 삭제하게 될 수도 있습니다.

데이터의 허수 용량 차지 방지와 사용공간 확보를 틈틈이 해주기 위해 `VACUUM`을 사용했습니다.

우선, 용량 확인을 위해 `manage.py`가 있는 디렉토리에서 `ls -al`을 입력해줍니다.

`db.sqlite3`의 파일크기에 대한 확인입니다.

[![img](https://user-images.githubusercontent.com/88086271/141416947-0d02def3-cfa9-4961-9767-56db730fa91e.png)](https://user-images.githubusercontent.com/88086271/141416947-0d02def3-cfa9-4961-9767-56db730fa91e.png)

`sqlite3`을 실행하고, 데이터가 가장 많은 테이블을 삭제했습니다.

[![img](https://user-images.githubusercontent.com/88086271/141417208-c4198d1a-a4ff-44ea-abad-3734fa10674b.png)](https://user-images.githubusercontent.com/88086271/141417208-c4198d1a-a4ff-44ea-abad-3734fa10674b.png)

`sqlite3`을 종료하고 크기를 확인해보면, 테이블을 삭제했음에도 불구하고 `db.sqlite3`의 파일크기는 그대로인 걸 확인할 수 있습니다.

[![img](https://user-images.githubusercontent.com/88086271/141417351-521f74a8-8f67-40b5-bdb2-cd7134e6a5e0.png)](https://user-images.githubusercontent.com/88086271/141417351-521f74a8-8f67-40b5-bdb2-cd7134e6a5e0.png)

`sqlite3`에 접속해서 `vacuum`을 입력 후 다시 나와서 `ls -al`을 입력해보면 159,000에서 69,000으로 감소한 것을 알 수 있습니다.

이렇게 테이블 최적화를 통해 유효 데이터만 관리될 수 있도록 VACUUM을 우선으로 설정했습니다.

[![img](https://user-images.githubusercontent.com/88086271/141417656-d8132fdf-0c46-4115-a6e1-cb5696665529.png)](https://user-images.githubusercontent.com/88086271/141417656-d8132fdf-0c46-4115-a6e1-cb5696665529.png)

- #### **Indexing**

![](https://user-images.githubusercontent.com/61782539/141482697-6ff59772-441a-4a9a-95f3-7734127ceb64.png)

거래내역을 조회할 때 filter와 order_by에 사용되는 created_at 필드에 index가 생성되도록 하여 테이블의 데이터가 많아도 빠른 검색이 가능하도록 보완하였습니다.

- #### partitioning

이번 과제를 진행하면서, 1억건이 넘는 데이터가 생성되었을 때 테이블에 대한 관리를 고민하면서 파티셔닝에 대한 개념을 처음 접하게 되었습니다. 1억건이 넘는 거래내역을 거래기간에 따라 RANGE PARTITION을 적용하여 여러개의 테이블로 나누어 저장하면, 논리적으로는 하나의 테이블처럼 보이지만 DBMS 내부적으로 거래일자에 따라 각 파티션의 데이터를 조회하므로 만약 해당 거래기간이 속한 테이블에 데이터가 500만건이라고 하면 500만건의 데이터가 있는 테이블만 조회할 수 있게 됩니다. 또 RANGE PARTITION은 데이터 보관주기를 관리할 때 보관기간이 지난 파티션 테이블만 삭제하면 되기 때문에 금융거래 내역을 관리하는데도 유용하게 사용될 수 있습니다.



파티셔닝을 프로젝트에 적용해보기 위해 Architect 패키지를 사용해보았습니다. 

```python
from django.db import models
import architect

@architect.install('partition', type='range', subtype='integer',
                   constraint='100', column='id')
class User(models.Model):
    name     = models.CharField(max_length = 50)
    email    = models.CharField(max_length = 200, unique = True)
    password = models.CharField(max_length = 500)

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.name
```

먼저 잘 적용이 되는지 확인하기 위해 User 모델에 적용 후에 명령어를 실행하였습니다.

```
architect partition --module users.models
architect partition: result: successfully (re)configured the database for the following models: User
```

후에 constraint에 설정된 범위에 따라 여러 범위의 id값을 가진 user를 생성해보았지만 User 테이블에 파티션이 적용되지 않았습니다.

Architect의 공식문서를 찾아보니 PostgreSQL과 MySQL 두 db를 지원하고 sqlite3는 지원하지 않는다는 것을 알았습니다.

- Supported DBs
  - [PostgreSQL](https://www.postgresql.org/) >= 8.0
  - [MySQL](https://www.mysql.com/) >= 5.5

django-db-parti https://pypi.org/project/django-db-parti/ 라는 다른 패키지도 찾아보았지만 해당 패키지도 PostgreSQL과 MySQL만 지원하였습니다.



저희 팀은 시간이 얼마 남지 않은 상황에서 차라리 모델링 차원에서라도 하나의 테이블로 관리되던 거래내역 테이블을 년도에 따라 따로 생성하여 관리하는 것으로 미약하게나마 구현해보는 것이 좋겠다고 판단하였습니다. 따라서 deals 테이블을 2021년 거래내역이 저장돼있는 deals2021 테이블과 2020년 거래내역이 저장돼있는 deals2020 테이블로 분할되도록 모델을 수정하였습니다.

![](https://user-images.githubusercontent.com/61782539/141502990-2fc032aa-e997-4e72-9261-60ba96e9e84b.png)

deals2020 테이블에는 2020년도에 생성된 거래내역 데이터만 저장돼있습니다.

![](https://user-images.githubusercontent.com/61782539/141503320-74a2b342-529c-4da1-a496-a2d4d3035722.png)

deals2021 테이블에는 2021년도에 생성된 거래내역 데이터만 저장돼있습니다.



이렇게 모델링을 수정한 후에 거래내역을 조회하는 API에서 조회한 거래기간의 시작날짜 연도가 2020년일 때만 deals2020 테이블에 접근하여 조회한 기간에 포함되는 데이터를 가져오고, 조회한 기간이 2021년에 국한되면 deals2021 테이블의 데이터에만 접근하도록 구현하여 많은 양의 거래내역을 분할하여 접근할 수 있게 하였습니다. 또 2020년 데이터의 보관기간이 지났다고 했을 때 해당 테이블의 데이터만 삭제하면 되기 때문에 데이터 관리가 좀 더 용이할 것 같습니다.



2020-04-02 ~ 2021-11-12 거래내역 조회

```
/deals/1?start_date=2020-04-02&end_date=2021-11-12&sort=old&deal_position_id=&page=2
```

```sql
2021-11-13 02:31:37,353 DEBUG (0.095) SELECT "deals2020"."id", "deals2020"."account_id", "deals2020"."deal_position_id", "deals2020"."amount", "deals2020"."created_at", "deals2020"."balance", "deals2020"."description", "deal_positions"."id", "deal_positions"."position" FROM "deals2020" INNER JOIN "deal_positions" ON ("deals2020"."deal_position_id" = "deal_positions"."id") WHERE (django_datetime_cast_date("deals2020"."created_at", NULL, NULL) BETWEEN '2020-04-02' AND '2021-11-12' AND "deals2020"."account_id" = 1) ORDER BY "deals2020"."created_at" ASC; args=('2020-04-02', '2021-11-12', 1)
2021-11-13 02:31:37,716 DEBUG (0.068) SELECT "deals2021"."id", "deals2021"."account_id", "deals2021"."deal_position_id", "deals2021"."amount", "deals2021"."created_at", "deals2021"."balance", "deals2021"."description", "deal_positions"."id", "deal_positions"."position" FROM "deals2021" INNER JOIN "deal_positions" ON ("deals2021"."deal_position_id" = "deal_positions"."id") WHERE (django_datetime_cast_date("deals2021"."created_at", NULL, NULL) BETWEEN '2020-04-02' AND '2021-11-12' AND "deals2021"."account_id" = 1) ORDER BY "deals2021"."created_at" ASC; args=('2020-04-02', '2021-11-12', 1)
[13/Nov/2021 02:31:38] "GET /deals/1?start_date=2020-04-02&end_date=2021-11-12&sort=old&deal_position_id=&page=2 HTTP/1.1" 200 3548
```

deals2020 테이블과 deals2021 테이블에 접근합니다.



2021-04-02 ~ 2021-11-12 거래내역 조회

```
deals/1?start_date=2021-04-02&end_date=2021-11-12&sort=old&deal_position_id=&page=1
```

```sql
2021-11-13 02:34:27,308 DEBUG (0.099) SELECT "deals2021"."id", "deals2021"."account_id", "deals2021"."deal_position_id", "deals2021"."amount", "deals2021"."created_at", "deals2021"."balance", "deals2021"."description", "deal_positions"."id", "deal_positions"."position" FROM "deals2021" INNER JOIN "deal_positions" ON ("deals2021"."deal_position_id" = "deal_positions"."id") WHERE (django_datetime_cast_date("deals2021"."created_at", NULL, NULL) BETWEEN '2021-04-02' AND '2021-11-12' AND "deals2021"."account_id" = 1) ORDER BY "deals2021"."created_at" ASC; args=('2021-04-02', '2021-11-12', 1)
[13/Nov/2021 02:34:27] "GET /deals/1?start_date=2021-04-02&end_date=2021-11-12&sort=old&deal_position_id=&page=1 HTTP/1.1" 200 3550
```

deals2021 테이블에만 접근합니다.

### 10. Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 8퍼센트(eightpercent)에서 출제한 과제를 기반으로 만들었습니다. 감사합니다.
