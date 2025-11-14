프롬프트 유형과 선택 이유

추천 프롬프트 유형

지시형(Instructional) 프롬프트 — “너는 주니어 PM의 추상적 아이디어를 개발자·디자이너가 바로 작업할 수 있는 수준의 상세 요구사항으로 변환하는 전문가다. 아래 정보를 바탕으로…” 처럼 직접적 지시를 줌.
이유: 목표가 구체적 산출물(기능 목록, DB 설계, 유저 플로우) 이므로 결과 형식을 강하게 고정해야 개발·디자인 산출물로 바로 연결될 수 있음.

템플릿 + 예시 제공 프롬프트 — 출력 포맷(기능 항목, API, DB 스키마, 페이지별 와이어 설명 등)을 템플릿으로 명시하고, 예시 항목을 하나 넣어 기대 형식을 보여줌.
이유: 사용자가 기대하는 형식(예: 표, 리스트, 엔드포인트 샘플)을 명확히 보여주면 모델이 일관된, 재현 가능한 산출물을 만듦.

검증/체크리스트 포함 프롬프트 — “출력 뒤에 개발자가 확인할 체크리스트(우선순위, 수용조건, 테스트 케이스)를 반드시 덧붙여라.”
이유: 킥오프에서 불확실성 감소, 실제 개발 착수 가능성 증가.

작성 위해 추가로 필요한 요건 (즉시 수집하면 더 정확해짐)

대상 사용자(타깃) 정보: 연령대, 영양지식 수준, 건강 상태(예: 일반 성인, 당뇨 환자 등).

지원 범위(국가/언어, 단위: kcal / kJ 등): 한국 대상인가, 다국어 지원 예정인가.

MVP 범위 우선순위: ‘빠르게 검증할 핵심 기능’ 3개를 고르면 무엇인가? (예: 식단 입력 → 칼로리 계산 → 개인 대시보드)

데이터 보안/규정 제약: 민감 건강정보 저장 여부, 개인정보보호 수준(암호화, GDPR/국내법 등).

통합 예정 서비스: 외부 식품 DB, OCR, 영양소 데이터셋 등 연동 계획 유무.

디자인 제약: 브랜드 가이드(색상·타입), 반응형 필요성(모바일 우선?).

기술 스택 선호(있다면): 프론트엔드(React, Vue), 백엔드(Node/Django), DB(Postgres/Mongo).

없으면 기본 가정으로 진행하되(한국/원-언어, kcal, React + Node(Postgres)) 명시해 둠.

문제 해결 프롬프트 (사용자가 AI에 입력할 실제 프롬프트 — 한국어)
너는 제품 요구사항 전문가이자 풀스택 엔지니어 관점의 PM이다.
아래 배경과 가정으로 '뉴트리 가이드(Nutri-Guide)'의 MVP 웹 프로토타입을 개발팀과 디자이너가 즉시 작업할 수 있도록 **상세 요구사항 리스트**를 만들어라.

[배경/목표]
- 서비스: 개인 맞춤형 영양 관리 웹(MVP)
- 핵심 가치: 사용자가 식단을 입력하면 각 음식의 칼로리 및 주요 영양소를 계산해 개인 대시보드에 보여준다.
- 대상: 일반 성인(한국), kcal 단위 사용
- 가정(없을 경우 기본): React 프론트엔드, Node.js/Express 백엔드, PostgreSQL, 인증은 이메일 기반

[출력 형식 — 반드시 지킬 것]
1. **MVP 기능 목록(우선순위: P0/P1/P2)** — 각 기능에 간단한 설명, 수용조건(acceptance criteria), 관련 화면 또는 API 표기
2. **사용자 흐름(User Flow)** — 주사용자 시나리오 2개(새 사용자 가입 → 첫 식단 입력 → 대시보드 확인 / 기존 사용자: 빠른 식단 입력 → 일별 리포트)
3. **페이지 구조 및 와이어(페이지별 요소)** — 각 페이지(로그인, 가입, 식단 입력, 대시보드, 리포트, 설정 등)에서 필요한 컴포넌트·데이터 표시 항목 목록
4. **데이터 요구사항 & DB 스키마(테이블, 주요 필드, 관계)** — sample SQL 타입 포함
5. **백엔드 API 설계(엔드포인트 목록, 요청/응답 샘플)** — 인증·식단 입력·칼로리 계산·리포트 조회 등
6. **비기능 요구사항(보안, 성능, 접근성, 로깅 등)** — 간단 우선순위
7. **디자이너/개발자용 킥오프 체크리스트** — 초기 스프린트에 필요한 작업 항목(와이어·API 계약·테스트 데이터 등)
8. **테스트·수용 기준(간단한 E2E 시나리오 3개)**

제한: 출력은 한국어로, 간결한 표/목록 중심으로. 총 분량은 너무 길어지지 않게(한 번에 읽기 좋은 분량), 그러나 개발에 바로 쓰기 충분한 수준으로 구체화하라.

프롬프트 실행 결과

(아래는 위 프롬프트를 실행한 결과 — 개발·디자인 팀이 킥오프에서 바로 쓸 수 있도록 정리)

1) MVP 기능 목록 (우선순위)

P0 (필수 — 릴리스 전 반드시 구현)

회원가입 / 로그인 (이메일+비밀번호, JWT 세션)

수용조건: 이메일 가입 후 로그인 가능, 토큰으로 인증된 API 호출 허용.

관련: /api/auth/register, /api/auth/login

식단 입력(수동) — 한 식사에 여러 음식 추가 가능

수용조건: 음식명, 섭취량(단위: g/ml/개), 시간, 식사 유형(아침/점심/저녁/간식) 입력 후 저장.

관련: /api/meals POST

칼로리·주요 영양소 계산 (입력 시 백엔드에서 계산)

수용조건: 음식별 kcal, 탄수화물, 단백질, 지방을 식품 DB 또는 기본 데이터로 산출해 저장 및 반환.

관련: 칼로리 서비스 모듈(식품 DB 참조)

일별 요약 대시보드 표시(오늘 칼로리 합계, 영양소 비율, 최근 식사 목록)

수용조건: 로그인 후 대시보드에서 오늘 데이터 확인 가능.

간단한 리포트(일별/주별) CSV 또는 화면 그래프(값 표출)

수용조건: 특정 기간 선택 시 총 kcal, 평균 kcal/day, 영양소 합계 제공.

P1 (중요 — 다음 릴리즈 고려)
6. 음식 검색/자동완성(내장 식품 DB 기반)
7. 식단 편집·삭제 이력 관리
8. 프로필(키, 체중, 목표 칼로리) — 기본 개인화

P2 (추후)
9. 사진/OCR 인식으로 식단 자동 입력
10. 외부 식품 DB 연동(공공 API/상업 DB)
11. 소셜/공유 기능

2) 사용자 흐름 (두 가지 시나리오)

시나리오 A — 신규 사용자: 가입 → 첫 입력 → 대시보드 확인

사용자: 홈페이지 방문 → “회원가입” 클릭

가입 폼(이메일, 비밀번호, 닉네임, 키/몸무게(선택)) 제출 → 이메일 인증(생략 가능, MVP에서는 선택)

첫 로그인 후 “식단 입력” 가이드 모달(한 줄 설명) 노출

식단 입력 페이지에서 ‘음식명’, ‘섭취량’, ‘식사 유형’ 입력 → 저장

계산 완료 후 대시보드로 리다이렉트 → 오늘 총 kcal 및 영양소 비중 확인

시나리오 B — 기존 사용자: 빠른 입력 → 일별 리포트 확인

로그인 → 상단 빠른 입력(모달) 사용하여 식단 추가 후 저장

대시보드에서 ‘지난 7일’ 리포트 버튼 클릭 → 주간 리포트 화면에 평균 kcal/day, 날짜별 막대그래프 제공

3) 페이지 구조 및 와이어(요소별)

로그인 페이지

이메일, 비밀번호 필드, 로그인 버튼, 비밀번호 찾기, 회원가입 링크

회원가입 페이지

이메일, 비밀번호, 닉네임, (선택) 키/몸무게/목표 kcal

대시보드 (홈)

헤더: 사용자 프로필 요약, 빠른 입력 버튼

카드: 오늘 총 칼로리, 목표 대비 퍼센트

파이/바 차트: 영양소 비율(탄수/단백/지방)

최근 식사 리스트(시간, 음식명, kcal)

주간 요약 링크

식단 입력 페이지 / 모달

음식 검색(자동완성) / 직접 입력 탭

섭취량 입력(숫자 + 단위 드롭다운), 식사 유형, 시간, 메모

저장 버튼(저장 시 서버에 POST)

리포트 페이지

기간 선택(오늘/7일/30일/커스텀)

표: 날짜별 칼로리 합계

그래프: 일별 막대, 영양소 트렌드

CSV 내보내기 버튼

프로필 / 설정

개인정보, 키/체중/목표, 알림 설정, 데이터 다운로드/삭제

4) 데이터 요구사항 & DB 스키마 (샘플 — PostgreSQL 기준)

테이블: users

id: UUID PK

email: varchar UNIQUE NOT NULL

password_hash: varchar NOT NULL

nickname: varchar

height_cm: integer NULL

weight_kg: decimal NULL

target_kcal: integer NULL

created_at, updated_at (timestamps)

테이블: foods (내부 식품 DB: MVP는 기본 샘플 데이터 포함)

id: UUID PK

name: varchar NOT NULL

serving_size_g: integer (기본 제공량)

kcal_per_100g: decimal

carbs_g_per_100g: decimal

protein_g_per_100g: decimal

fat_g_per_100g: decimal

source: varchar (manual/system)

created_at, updated_at

테이블: meals (사용자가 생성한 식사 레코드)

id: UUID PK

user_id: UUID FK -> users(id)

meal_time: timestamp

meal_type: enum('breakfast','lunch','dinner','snack')

created_at, updated_at

테이블: meal_items (한 식사 내 음식 항목)

id: UUID PK

meal_id: UUID FK -> meals(id)

food_id: UUID NULL (참조 foods 또는 NULL이면 free-text)

name: varchar (사용자 입력명)

amount: decimal (수치)

unit: enum('g','ml','개')

kcal: decimal (계산된 값)

carbs_g, protein_g, fat_g: decimal

created_at, updated_at

관계: users 1—N meals, meals 1—N meal_items, meal_items → optional foods

5) 백엔드 API 설계 (샘플)

인증

POST /api/auth/register

Body: { email, password, nickname?, height_cm?, weight_kg? }

Resp: { user:{id, email, nickname}, token }

POST /api/auth/login

Body: { email, password }

Resp: { token, user }

식사/식단

POST /api/meals — 새 식사 생성

Body: { meal_time, meal_type, items: [{food_id?|name, amount, unit}] }

Resp: { meal_id, computed_totals: {kcal, carbs, protein, fat}, items: [...] }

GET /api/meals?date=YYYY-MM-DD — 특정일 식사 목록

Resp: { date, meals: [...] }

PUT /api/meals/:id — 수정

DELETE /api/meals/:id

리포트

GET /api/reports/daily?start=YYYY-MM-DD&end=YYYY-MM-DD

Resp: { daily: [{date, total_kcal, carbs, protein, fat}], aggregate: {...} }

음식 DB

GET /api/foods?q=바나나&limit=10 — 자동완성

POST /api/foods — 관리자용 음식 추가(초기 데이터 업로드 스크립트로 대체 가능)

요청은 JWT in Authorization: Bearer <token>

6) 비기능 요구사항 (요약)

보안

비밀번호는 bcrypt(또는 argon2)로 해시 저장.

HTTPS 의무화.

JWT 만료: 액세스 1시간, 리프레시 토큰 사용 권장(선택).

개인정보(키/몸무게 등)는 암호화 고려(규정에 따라).

성능

첫 페이지(대시보드) 로드 ≤ 1.5s(경량 데이터).

식단 입력 시 계산 응답 ≤ 500ms(단순 DB 조회 + 연산).

가용성/로깅

에러 로깅(Sentry 등), API 호출 로그(보안, 디버깅 목적).

DB 백업 하루 1회.

접근성(A11Y)

폼 레이블 명확화, 키보드 네비게이션, 색 대비 기준 충족(AA).

7) 디자이너/개발자용 킥오프 체크리스트 (우선순위 포함)

디자인(우선)

 대시보드·식단 입력·리포트의 와이어프레임(모바일/데스크톱)

 디자인 시스템(버튼, 입력, 카드) 기본 스타일 가이드

개발(우선)

 인증 서비스(회원가입/로그인) 구현 및 토큰 검증 미들웨어

 음식 DB 샘플 업로드(상위 500개 흔한 식품)

 식단 입력 API + 칼로리 계산 모듈(단위 변환 포함)

 대시보드 API(오늘 요약)

 E2E 테스트(주요 시나리오 3개 자동화)

공통

 API 계약서(swagger/REST docs) 초안 작성

 개발용 더미 계정·테스트 데이터 준비

8) 테스트·수용 기준 (E2E 시나리오 3개)

회원가입·로그인 패스

가입 후 즉시 로그인 가능, 토큰으로 보호된 /api/meals 접근 성공.

식단 입력 → 대시보드 반영

특정 음식(바나나 100g) 입력 → 반환값에 kcal(예: 89kcal/100g) 포함, 대시보드 합계에 반영.

리포트 기간 조회

7일치 입력 후 주간 리포트 요청 → 날짜별 합계와 aggregate(총 kcal, 평균 kcal/day) 일치.

부가: 개발·디자인에 바로 줄 수 있는 간단 샘플(예시)

샘플 음식 레코드 (foods)

{ name: "바나나", serving_size_g: 100, kcal_per_100g: 89, carbs_g_per_100g: 23, protein_g_per_100g: 1.1, fat_g_per_100g: 0.3 }

칼로리 계산 예시 로직

kcal = (kcal_per_100g / 100) * amount_in_g

단위가 '개'이면 foods.serving_size_g * 개수 → g로 변환

