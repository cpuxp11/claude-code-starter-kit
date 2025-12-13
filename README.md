# Claude Code Starter Kit

> Claude Code를 처음 사용하는 분들을 위한 스타터 키트

## Claude Code란?

**Claude Code**는 터미널에서 실행되는 AI 코딩 어시스턴트입니다. 대화를 통해 코드 작성, 파일 관리, 작업 자동화를 수행할 수 있습니다.

### 주요 특징
- 자연어로 코딩 요청
- 파일 읽기/쓰기/편집
- 슬래시 명령어로 빠른 작업
- 외부 서비스 연동 (Skills)

---

## 완전 초보자 가이드

### Step 1: Node.js 설치

1. https://nodejs.org 접속
2. **LTS 버전** 다운로드 및 설치
3. 설치 완료 후 컴퓨터 재시작

### Step 2: 이 저장소 다운로드

**방법 A: Git Clone (추천)**
```bash
git clone https://github.com/YOUR_USERNAME/claude-code-starter-kit.git
cd claude-code-starter-kit
```

**방법 B: ZIP 다운로드**
1. 이 페이지 상단의 초록색 `Code` 버튼 클릭
2. `Download ZIP` 클릭
3. 다운로드된 ZIP 압축 해제
4. 원하는 위치로 폴더 이동

### Step 3: Claude Code 설치

Cursor (또는 VS Code) 열고 터미널 실행:
- **Windows**: `Ctrl + `` ` (백틱) 또는 상단 메뉴 Terminal → New Terminal
- **Mac**: `Cmd + `` ` 또는 상단 메뉴 Terminal → New Terminal

터미널에 입력:
```bash
npm install -g @anthropic-ai/claude-code
```

### Step 4: 폴더 열기 & 실행

1. Cursor에서 `File → Open Folder` → 다운로드한 폴더 선택
2. 터미널에서 `claude` 입력 후 Enter
3. `/daily-note` 입력하여 테스트

---

## 폴더 구조 (Johnny Decimal)

```
claude-code-starter-kit/
├── .claude/                    # Claude Code 설정 (건드리지 마세요)
│   ├── commands/               # 슬래시 명령어
│   ├── skills/                 # 외부 서비스 연동
│   └── agents/                 # 자동화 에이전트
├── 00-inbox/                   # 새 아이디어, 메모
├── 00-system/                  # 시스템 설정, 템플릿
├── 10-projects/                # 진행 중인 프로젝트
├── 20-areas/                   # 지속 관리 영역
├── 30-knowledge/               # 지식, 인사이트
├── 40-personal/                # 개인 노트 (Daily Notes, Todos)
└── 50-archive/                 # 완료/보관 자료
```

---

## 사용 가능한 명령어

### 기본 명령어 (바로 사용 가능)

| 명령어 | 설명 |
|--------|------|
| `/daily-note` | 오늘의 Daily Note 생성 |
| `/idea` | 아이디어 저장 |
| `/todo` | 할 일 추가 |
| `/todos` | 할 일 목록 보기 |
| `/setup-workspace` | 워크스페이스 설정 |

### 고급 명령어 (설정 필요)

| 명령어 | 설명 | 필요 설정 |
|--------|------|----------|
| `/crawl` | 웹페이지 크롤링 | Python, Playwright |

---

## Skills 설정 (선택사항)

Skills는 외부 서비스와 연동하는 기능입니다. **필수가 아닙니다!**

### Google Calendar 연동

```bash
pip install gcalcli
gcalcli init
```

이후 Claude에게 "오늘 일정 알려줘" 라고 말하면 됩니다.

### 웹 크롤링 (Playwright)

<details>
<summary><b>Mac / Linux</b></summary>

```bash
cd .claude/skills/web-crawler-ocr/scripts
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

</details>

<details>
<summary><b>Windows</b></summary>

```bash
cd .claude\skills\web-crawler-ocr\scripts
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

</details>

설정 완료 후 `/crawl https://example.com` 으로 사용

---

## 자주 묻는 질문

### Q: "명령어가 실행되지 않아요"
**A:** `.claude/` 폴더가 워크스페이스 최상위에 있는지 확인하세요.

### Q: "'claude' 명령어를 찾을 수 없어요"
**A:** Node.js 설치 후 터미널을 재시작하세요. 안 되면 `npm install -g @anthropic-ai/claude-code` 다시 실행.

### Q: "npm 명령어를 찾을 수 없어요"
**A:** Node.js가 설치되지 않았습니다. https://nodejs.org 에서 LTS 버전 설치하세요.

### Q: "크롤링이 안 돼요"
**A:**
- **Mac**: `source venv/bin/activate` 실행했는지 확인
- **Windows**: `venv\Scripts\activate` 실행했는지 확인
- Playwright 설치: `playwright install chromium`

### Q: "Daily Note가 생성되지 않아요"
**A:** `40-personal/41-daily/` 폴더가 존재하는지 확인하세요.

---

## 더 알아보기

- [Claude Code 공식 문서](https://docs.anthropic.com/claude-code)
- [Johnny Decimal 시스템](https://johnnydecimal.com)

---

**Made with love for Claude Code beginners**
