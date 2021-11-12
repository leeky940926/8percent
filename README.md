테스트 시나리오만 작성 ( 이대로 포스트맨 테스트한 거 포스트맨 문서에 반영해주세요 현우님 )

일단 users.id = 1 인 사람의 정보는 정상적으로 변경해주세요(ex. name='박현우', email='hwpark@8percent.com')
그리고 banks에 은행 하나 추가해주세요 (ex. 농협)
그 다음 accouts에 데이터 하나 추가해주세요 (ex. owner_id=1, bank_id=5, number='3981425532143', balance=1000000)
시나리오 테스트에 대한 포스트맨 request&response도 시나리오 아래 같이 첨부해주세요

0. 시나리오
: 박현우("hwpark@8percent.com")는 오늘 월급일 및 카드대금결제일이며, 입/출금이 잘 이루어졌는지 로그인해서 확인 해보려고 함
입/출금은 구현된 API를 통해 거래내역에 추가되며, 마지막 시나리오에서 조회 예정

박현우("hwpark@8percent.com")는 신한은행(banks.id=1)과 농협(banks.id=5)에 계좌가 존재하며, 농협 계좌에서 입출금을 진행할 예정
농협에는 현재 1,000,000원의 잔액(accounts.balance)이 남아있음


1. 로그인

1-1. 아이디 오입력
이메일을 잘못 기억하고 있어서 "parkhw@8percent.com"로 입력 후 로그인 시도
(email : "parkhw@8percent.com", password="test"로 request.body 작성해서 테스트) 

1-2. 비밀번호 오입력
비밀번호를 빠르게 입력하려다가 실수로 잘못된 비밀번호를 입력 후 로그인 시도
(email : "hwpark@8percent.com", password="tset"로 request.body 작성해서 테스트)

1-3. 로그인 성공
이메일과 비밀번호를 올바르게 입력해서 로그인에 성공했으며, 토큰까지 발급 완료
(email : "hwpark@8percent.com", password="test" 입력 후 토큰 발급 받은 것까지 request.body에 작성해서 테스트)


2. 입금/출금

2-1. 입금
매월 12일은 월급날이며, 세후 수령액은 2,800,000원임
(bank_id=5, account_id=26, deal_position_id=1, amount=2800000, description="10월 급여" 로 request.body 작성해서 테스트)

2-2. 출금
매월 12일은 카드대금결제일이며, 이번 달 결제액은 80,0000원임
(bank_id=5, account_id=26, deal_position_id=2, amount=800000, description="11월 카드대금결제" 로 request.body 작성해서 테스트)

2-3. 잔액초과금액 출금
현재 계좌에는 3,000,000원이 남아있는 상태이며, 4,000,000원 상당의 컴퓨터를 할부로 구매해야 되는데, 직원이 실수로 일시불결제를 누름
이 때, 계좌잔액의 초과금액을 결제 요청한것이기 때문에 "CANNOT_REQUEST_EXCEED_BALANCE"라는 문구와 함께 에러코드는 400을 리턴
(bank_id=5, account_id=26, deal_position_id=2, amount=4000000, description="컴퓨터 구매" 로 request.body 작성해서 테스트)

3. 거래내역 조회
