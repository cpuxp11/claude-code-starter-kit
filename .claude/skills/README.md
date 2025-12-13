# Skills

> Claude Code와 외부 서비스를 통합하는 기능 모음

## 📖 Skills란?

Skills는 Claude Code를 외부 서비스와 연결하여 확장하는 기능입니다.

| 구분 | Skills | Commands |
|------|--------|----------|
| **목적** | 외부 서비스 통합 | 내부 워크플로우 자동화 |
| **예시** | Google Calendar, Web Crawler | `/daily-note`, `/idea` |
| **설정** | OAuth, API 키 필요 | 설정 불필요 (즉시 사용) |

---

## 🎯 사용 가능한 Skills

### ✅ Google Calendar (gcalcli 기반)

**설정 난이도**: ⭐⭐ (10분)

Google Calendar를 Claude와 통합하여 대화만으로 일정 관리:
- "오늘 일정 뭐 있어?"
- "이번 주 스케줄 알려줘"
- "내일 오후 3시 미팅 잡아줘"

**빠른 시작**:
```bash
# 1. gcalcli 설치
pip install gcalcli
# 또는
brew install gcalcli  # Mac

# 2. OAuth 인증
gcalcli init

# 3. Claude와 대화
"오늘 일정 알려줘"
```

자세한 내용: [google-calendar/SKILL.md](./google-calendar/SKILL.md)

---

### ✅ Web Crawler + OCR (Playwright + EasyOCR)

**설정 난이도**: ⭐⭐⭐ (15분)

웹페이지 크롤링 + 이미지 OCR을 자동으로 처리:
- JavaScript SPA 사이트 지원 (GPTers 등)
- 한국어/영어 OCR
- API 비용 0원 (오픈소스)

**빠른 시작**:
```bash
# 1. 가상환경 설정
cd .claude/skills/web-crawler-ocr/scripts
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. 의존성 설치
pip install -r requirements.txt
playwright install chromium

# 3. 사용
/crawl https://example.com
```

자세한 내용: [web-crawler-ocr/scripts/](./web-crawler-ocr/scripts/)

---

## ⚠️ 중요

**Skills는 선택사항입니다!**

- Commands (`/daily-note` 등)는 바로 사용 가능
- Skills는 추가 설정이 필요
- 필요한 기능만 설정하세요
