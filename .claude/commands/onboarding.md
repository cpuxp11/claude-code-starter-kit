---
description: 워크스페이스 초기 설정 (폴더 생성 + 템플릿)
allowed-tools: Write, Read, Bash, Edit
---

# 워크스페이스 온보딩

처음 시작하는 분을 위해 폴더 구조와 템플릿을 자동 생성합니다.

## Step 1: 질문 2개

**Q1:** 워크스페이스 이름을 정해주세요 (예: my-notes, work-docs, pkm)

**Q2:** 어떤 용도인가요?
- A) 개인 지식관리
- B) 업무/프로젝트
- C) 둘 다

---

## Step 2: 폴더 구조 생성

답변을 받으면 **현재 작업 디렉토리**에 다음 구조를 생성하세요:

```
{워크스페이스명}/
├── 00-inbox/           # 임시 저장소
├── 00-system/
│   └── 01-templates/   # 템플릿
├── 10-projects/        # 프로젝트
├── 20-areas/           # 지속 관리 영역
├── 30-knowledge/
│   └── 33-insights/    # 인사이트
├── 40-personal/
│   ├── 41-daily/       # Daily Notes
│   └── 46-todos/       # 할 일
└── 50-archive/         # 보관함
```

Bash로 폴더 생성:
```bash
WORKSPACE="{사용자 입력}"
mkdir -p "$WORKSPACE/00-inbox"
mkdir -p "$WORKSPACE/00-system/01-templates"
mkdir -p "$WORKSPACE/10-projects"
mkdir -p "$WORKSPACE/20-areas"
mkdir -p "$WORKSPACE/30-knowledge/33-insights"
mkdir -p "$WORKSPACE/40-personal/41-daily"
mkdir -p "$WORKSPACE/40-personal/46-todos"
mkdir -p "$WORKSPACE/50-archive"
```

---

## Step 3: 기본 파일 생성

Write 도구로 다음 파일들을 생성하세요:

### 3-1. `{workspace}/00-inbox/README.md`
```markdown
# Inbox

새 메모, 아이디어, 크롤링 결과가 여기 저장됩니다.

## 명령어
- `/idea` - 아이디어 저장
- `/crawl <URL>` - 웹페이지 크롤링

## 규칙
- 일주일에 한 번 정리
- 오래된 항목은 적절한 폴더로 이동
```

### 3-2. `{workspace}/00-system/01-templates/daily-note-template.md`
```markdown
# {{date}} Daily Note

## 오늘의 일정

## 오늘의 목표
- [ ]

## 메모


## 배운 것


## 관련 노트

```

### 3-3. `{workspace}/40-personal/46-todos/active-todos.md`
```markdown
# Active Todos

## 긴급
- [ ]

## 이번 주
- [ ]

## 나중에
- [ ]
```

---

## Step 4: 완료 안내

```
워크스페이스 설정 완료!

생성된 폴더:
- 00-inbox/     : 임시 메모
- 10-projects/  : 프로젝트
- 40-personal/  : Daily Note, 할 일

명령어:
- /daily-note  : 오늘 노트 생성
- /idea        : 아이디어 저장
- /crawl <URL> : 웹 크롤링

시작: "/daily-note" 입력해보세요!
```

---

## 실행 순서

1. Q1, Q2 질문
2. 답변 받으면 mkdir로 폴더 생성
3. Write로 README, 템플릿 생성
4. 완료 메시지 출력
