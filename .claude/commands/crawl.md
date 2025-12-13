---
description: Playwright로 URL 크롤링 (JS/SPA 지원, OCR 포함)
argument-hint: <URL> [output.md]
allowed-tools: Bash, Read
---

URL을 Playwright로 크롤링합니다. JavaScript SPA 사이트도 완벽 지원합니다.

**입력된 URL**: $ARGUMENTS

## 사전 준비

크롤링 스킬이 설정되어 있어야 합니다:

**Mac/Linux:**
```bash
cd .claude/skills/web-crawler-ocr/scripts
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

**Windows:**
```bash
cd .claude\skills\web-crawler-ocr\scripts
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## 실행

URL이 입력되지 않았으면 사용자에게 URL을 요청하세요.

URL이 있으면 OS에 맞는 명령어를 실행하세요:

**Mac/Linux:**
```bash
cd ".claude/skills/web-crawler-ocr/scripts" && \
source venv/bin/activate && \
python3 web-crawler-v2.py $ARGUMENTS
```

**Windows:**
```bash
cd ".claude\skills\web-crawler-ocr\scripts" && \
venv\Scripts\activate && \
python web-crawler-v2.py $ARGUMENTS
```

## 결과 처리

1. 생성된 마크다운 파일 경로 확인 (기본: `./00-inbox/`)
2. 파일 내용 요약 제공
3. 필요시 전체 내용 표시

## 기능

- JavaScript/SPA 완벽 지원 (GPTers 등)
- 이미지 OCR 자동 (한국어/영어)
- 포스트 링크 추출
- API 비용 0원
