---
name: google-calendar
description: Google Calendar 일정 조회, 검색, 등록. "일정", "스케줄", "캘린더" 등을 언급하면 자동 실행. Daily Note 작성, Weekly Review에 사용.
allowed-tools: Bash, Read
---

# Google Calendar Integration Skill

이 Skill은 **gcalcli**를 사용하여 Google Calendar와 통합합니다.

## ⚠️ 중요 규칙

### 일정 제목 작성 규칙
**제목에 날짜/시간 절대 포함 금지**

- ❌ "2025-11-13 13:00 커피챗"
- ❌ "11월 13일 알파브라더스"
- ✅ "알파브라더스 채중규 대표 커피챗"
- ✅ "HFK 겨울시즌 1회차: AI 파트너 만들기"

---

## 🎯 주요 기능

### 1. 일정 조회

```bash
# 오늘 일정
gcalcli agenda

# 특정 날짜 일정
gcalcli agenda 2025-11-13

# 특정 기간 일정
gcalcli agenda 2025-11-13 2025-11-15

# 특정 캘린더만 조회
gcalcli agenda --calendar "Work"
```

### 2. 일정 검색

```bash
# 기본 검색
gcalcli search "검색어"

# 특정 캘린더에서만 검색
gcalcli search "미팅" --calendar "Work"
```

### 3. 일정 추가

```bash
gcalcli add --calendar "캘린더명" \
  --when "YYYY-MM-DD HH:MM" \
  --duration 분 \
  --title "제목" \
  --where "장소" \
  --description "설명"
```

**예시**:
```bash
gcalcli add --calendar "Work" \
  --when "2025-11-13 13:00" \
  --duration 60 \
  --title "팀 미팅" \
  --where "회의실 A"
```

### 4. 일정 삭제

```bash
# 자동 삭제 (확인 없이)
gcalcli delete "검색어" --iamaexpert
```

---

## 📝 PKM 통합

### Daily Note (`/daily-note`)

Daily Note 생성 시 Google Calendar 일정을 자동으로 가져옵니다.

**Daily Note 예시**:
```markdown
### 📅 스케줄

#### Google Calendar
- **13:00-14:00**: 팀 미팅
- **15:00-16:00**: 1:1 미팅
```

---

## 💡 캘린더 종류

```bash
# 캘린더 목록 확인
gcalcli list
```

---

## ⚠️ 사전 준비

### 설치 방법

**자동 설치 (권장)**:
```bash
# /setup-google-calendar 커맨드 실행
```

**수동 설치**:
```bash
# 1. pipx 설치
brew install pipx  # macOS
# 또는
python3 -m pip install --user pipx

# 2. gcalcli 설치
pipx install gcalcli
pipx ensurepath
export PATH="$HOME/.local/bin:$PATH"

# 3. OAuth 인증
gcalcli init
```

---

## 🔧 트러블슈팅

### "gcalcli가 설치되지 않았습니다"
```bash
pipx install gcalcli
pipx ensurepath
export PATH="$HOME/.local/bin:$PATH"
```

### OAuth 인증 문제
```bash
rm ~/.gcalcli_oauth
gcalcli init
```

---

## 📚 참고 자료

- gcalcli 공식 문서: https://github.com/insanum/gcalcli
- 모든 명령어: `gcalcli --help`
