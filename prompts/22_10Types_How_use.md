## 프롬프트  
너는 30년차 프로토타입 개발자, 엔지니어, 갈등 조정자야. [가상 문제 상황]을 참고하여 다음의 항목들을 채워줘.  
[가상 문제 상황] 스크랩  
[출력값]  
1. 프롬프트 유형과 선택 이유  
2. 작성 위해 추가 필요 요건  
3. 문제 해결 프롬프트  

---

### 1. 프롬프트 유형과 선택 이유

**유형:** 🧩 “역할 기반 실전 프로토타입 생성 프롬프트” (Role-based Rapid Prototyping Prompt)

**선택 이유:**
- 단순 코드 요청이 아니라, UI/UX·디자인·운영 요구를 동시에 조율해야 함.  
- 회의 전 빠른 의사결정용으로 시각적·기능적 시연이 가능한 HTML/CSS/JS 단일 페이지 필요.  
- 이 프롬프트는 AI가 “프론트엔드 개발자 + UX 조율자”처럼 사고하며,  
  다양한 요구를 균형 있게 반영한 중립적 프로토타입을 생성하도록 설계됨.  

---

### 2. 작성 위해 추가 필요 요건

| 구분 | 필요 정보 | 이유 |
|:--|:--|:--|
| 🎨 UI/UX 방향 | 다크 모드 기본값 / 직관적 인터페이스 | 디자인팀과 기획팀 요구 절충 |
| 🎬 콘텐츠 구조 | 영상 플레이어, 댓글 타임스탬프 리스트, 승인/반려 버튼 | 운영팀 요구 반영 |
| 🧠 상호작용 | 타임스탬프 클릭 시 영상 이동 / 버튼 hover 반응 | ‘작동하는 느낌’을 주는 시연용 |
| 🧩 기술 스택 | HTML, CSS(내장), JS(순수 또는 ES6), 외부 라이브러리 無 | 빠른 실행과 수정 편의성 확보 |
| ⚙ 코드 구조 | 명확한 주석 / 섹션별 구분 / 함수 단위 이벤트 정의 | 회의 중 실시간 수정 용이 |
| 🕒 제작 목적 | 시연·피드백용 (프로덕션용 아님) | MVP로 명시해 기대치 조율 |

---

### 3. 문제 해결 프롬프트 (AI에게 줄 입력 예시)

아래는 ChatGPT나 Copilot, Claude 등 코드 생성 AI에 직접 입력할 수 있는 최적화된 명령문입니다 👇  

---

#### 🧠 [문제 해결 프롬프트 예시]

너는 30년차 프론트엔드 프로토타입 엔지니어이자 갈등 조정자다.  
다음 요구사항을 만족하는 **의사결정용 단일 페이지 웹 프로토타입(HTML/CSS/JS)**을 작성하라.  

📌 **목표:** 오늘 오후 회의에서 이해관계자들이 즉시 UI를 보고 의견을 조율할 수 있도록,  
코드 구조가 단순하고 수정이 쉬운 MVP 형태로 만든다.  

**요구사항:**  
- 페이지는 다크 모드 스타일을 기본으로 한다.  
- 상단에는 회사 로고 영역과 프로젝트 제목(“영상 리뷰 대시보드”)을 표시한다.  
- 중앙에는 HTML5 영상 플레이어를 배치한다.  
- 오른쪽 사이드바에는 타임스탬프별 댓글 목록을 표시하며, 클릭 시 영상이 해당 시점으로 이동한다.  
- 하단에는 승인(✅ Approve), 반려(❌ Reject) 버튼을 두고, 클릭 시 콘솔에 선택 로그를 남긴다.  
- 전체 UI는 Flex 또는 Grid 기반 반응형 구조로, 명확히 섹션 구분되어야 한다.  
- CSS와 JS는 같은 파일 안에 작성하되, 주석으로 섹션을 명확히 구분할 것.  
- 외부 라이브러리 없이 HTML, CSS, JS만 사용한다.  

**출력 형식:**  
- 완전한 HTML 문서 (doctype 포함)  
- 내부에 `<style>`과 `<script>` 블록 포함  
- 각 섹션별로 주석 명시: `/* HEADER */`, `/* VIDEO SECTION */`, `/* COMMENTS */`, `/* ACTION BUTTONS */`, `/* SCRIPT */`  

**추가 조건:**  
- 디자인은 심플하지만 트렌디한 느낌 (예: glassmorphism 효과 or subtle shadows)  
- 회의 중 수정이 쉽도록 주요 색상·폰트는 상단 변수로 정의할 것.  
- 버튼 hover 시 색상 변화로 피드백 제공.  

---

## 실행 결과

```html
<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>영상 리뷰 대시보드 — 프로토타입</title>

<style>
/* =========================
   /* THEME VARIABLES (상단에서 수정하기 쉬움) */
   ========================= */
:root{
  --bg: #0b0f13;
  --panel: rgba(255,255,255,0.03);
  --glass: rgba(255,255,255,0.04);
  --accent: #6ee7b7;          /* primary accent */
  --accent-2: #7cc3ff;        /* secondary */
  --muted: rgba(255,255,255,0.6);
  --danger: #ff7a7a;
  --success: #90ee90;
  --radius: 12px;
  --shadow: 0 6px 18px rgba(2,6,23,0.6);
  --font-sans: "Inter", "Segoe UI", Roboto, "Helvetica Neue", Arial;
}

/* =========================
   /* GLOBAL RESET & BASE
   ========================= */
* { box-sizing: border-box; }
html,body { height:100%; }
body{
  margin:0;
  font-family: var(--font-sans);
  background: linear-gradient(180deg, #07090b 0%, #0d1114 100%);
  color: #e6eef8;
  -webkit-font-smoothing:antialiased;
  padding:24px;
}

/* =========================
   /* LAYOUT
   ========================= */
.container{
  max-width:1200px;
  margin:0 auto;
  display:flex;
  gap:20px;
  align-items:flex-start;
  justify-content:space-between;
  min-height: calc(100vh - 48px);
}

/* HEADER */
.header{
  display:flex;
  align-items:center;
  gap:12px;
  margin-bottom:18px;
}
.logo{
  display:flex;
  align-items:center;
  gap:10px;
  padding:10px 14px;
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  border-radius: 10px;
  box-shadow: var(--shadow);
}
.logo .badge{
  width:40px;height:40px;border-radius:8px;
  display:flex;align-items:center;justify-content:center;
  background: linear-gradient(135deg, rgba(110,231,183,0.14), rgba(124,195,255,0.08));
  font-weight:700;color:var(--accent);
}
.title{ font-size:1.05rem; font-weight:600; letter-spacing: -0.2px; }

...
