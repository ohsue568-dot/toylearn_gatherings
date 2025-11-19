{
  "project_info": {
    "title": "개인 포트폴리오 웹사이트 제작",
    "description": "개발자·디자이너 역량을 보여주는 반응형 웹 포트폴리오. 최소 1개의 CRUD 기능 포함, 관리자 페이지를 통한 콘텐츠 관리 가능.",
    "goals": [
      "개인의 프로젝트와 경험을 직관적으로 보여주기",
      "최소 1개 이상의 실제 기능 구현(CRUD)",
      "관리자(Admin) 대시보드 구축",
      "재사용성 높은 컴포넌트 기반 UI 설계",
      "반응형 웹으로 모바일/PC 모두 최적화"
    ],
    "target_users": ["채용 담당자", "클라이언트", "협업 개발자"]
  },

  "tech_stack": {
    "frontend": {
      "html": "HTML5 시맨틱 구조 활용",
      "css": "CSS3, Flex/Grid, SCSS 선택 가능",
      "js": "Vanilla JS or React",
      "ui_framework_optional": ["TailwindCSS", "Bootstrap"]
    },
    "backend_optional": {
      "options": ["Node.js(Express)", "Firebase", "Supabase", "Django"],
      "reason": "CRUD 기능, Admin 인증을 위해 필요"
    },
    "database_optional": ["Firebase Firestore", "MongoDB", "MySQL", "Local JSON DB"]
  },

  "design_guide": {
    "style": {
      "concept": "Minimal & Professional",
      "color_palette": ["#111", "#ffffff", "#f4f4f4", "#0066ff"],
      "typo": [
        { "title": "H1: 32~40px", "weight": "700" },
        { "title": "Body: 14~16px", "weight": "400" }
      ]
    },
    "layout": {
      "header": "고정형 네비게이션 바",
      "section_basic": "80~120px 상하 여백",
      "grid_system": "모듈형 카드 레이아웃"
    },
    "accessibility": [
      "alt 태그 필수",
      "명도 대비 준수",
      "키보드 내비게이션 지원"
    ]
  },

  "site_structure": {
    "main_menu": [
      { "title": "Home", "type": "section", "content": "인트로 · 퍼스널 브랜딩" },
      { "title": "About", "type": "section", "content": "경력 / 스킬 / 자기소개" },
      { 
        "title": "Projects", 
        "type": "crud", 
        "content": "프로젝트 카드 목록",
        "crud_features": ["CREATE", "READ", "UPDATE", "DELETE"]
      },
      { "title": "Contact", "type": "form", "content": "문의 폼(메일 전송 또는 DB 저장)" }
    ],
    "admin_menu": [
      { "title": "Dashboard", "items": ["사이트 통계", "최근 문의"] },
      { 
        "title": "Project Manager",
        "description": "프로젝트 CRUD 기능 제공",
        "crud": {
          "create": "새 프로젝트 업로드",
          "read": "프로젝트 리스트",
          "update": "프로젝트 내용 수정",
          "delete": "프로젝트 삭제"
        }
      },
      { 
        "title": "Contact Manager",
        "description": "유저 문의 열람 및 삭제",
        "crud": ["READ", "DELETE"]
      },
      { "title": "Settings", "description": "프로필 이미지 및 소개 문구 수정" }
    ]
  },

  "core_features": {
    "frontend_components": [
      "헤더/푸터 공통 컴포넌트",
      "카드형 프로젝트 컴포넌트",
      "모달 상세 페이지",
      "관리자 전용 로그인 폼",
      "이미지 업로드 UI"
    ],
    "backend_features_optional": [
      "JWT 기반 Admin 인증",
      "REST API 구축",
      "파일 업로드 처리",
      "프로젝트 리스트 JSON 파일 자동 업데이트"
    ],
    "animations_optional": [
      "Fade-in 스크롤 효과",
      "프로젝트 카드 hover 효과"
    ]
  },

  "file_structure_template": {
    "root": {
      "index.html": "메인 페이지",
      "about.html": "소개",
      "projects.html": "프로젝트 목록",
      "project_detail.html": "상세",
      "contact.html": "문의",
      "admin": {
        "index.html": "관리자 로그인",
        "dashboard.html": "관리자 대시보드",
        "project_manager.html": "CRUD 페이지",
        "contact_list.html": "문의 관리"
      },
      "assets": {
        "css": ["reset.css", "style.css"],
        "js": ["main.js", "api.js", "admin.js"],
        "images": []
      },
      "data": ["projects.json", "contact.json"]
    }
  },

  "crud_example_json_structure": {
    "projects": [
      {
        "id": 1,
        "title": "포트폴리오 웹사이트",
        "description": "UI/UX 개선 및 CRUD 구현",
        "tech": ["HTML", "CSS", "JavaScript"],
        "thumbnail": "assets/images/project1.jpg",
        "url": "/project_detail.html?id=1"
      }
    ]
  },

  "deployment": {
    "options": ["GitHub Pages", "Netlify", "Vercel"],
    "guide": [
      "main 브랜치 기준 auto deploy",
      "assets 절대경로 대신 상대경로 사용",
      "admin 영역은 인증 없을 경우 외부 노출 금지"
    ]
  }
}
