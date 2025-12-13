---
name: google-calendar
description: Google Calendar 일정 조회, 검색, 등록. "일정", "스케줄", "캘린더" 등을 언급하면 자동 실행.
allowed-tools: Bash, Read
---

# Google Calendar Integration Skill

이 Skill은 **gcalcli**를 사용하여 Google Calendar와 통합합니다.

---

## ⚠️ 사전 준비

### gcalcli 설치
```bash
# Mac
brew install gcalcli
# 또는
pip install gcalcli
```

### OAuth 인증 (첫 사용 시)
```bash
gcalcli init
```
브라우저에서 Google 계정으로 로그인하고 권한을 승인하세요.

---

## 🎯 주요 기능

### 1. 일정 조회

```bash
# 오늘 일정
gcalcli agenda

# 특정 날짜 일정
gcalcli agenda 2025-01-15

# 특정 기간 일정
gcalcli agenda 2025-01-15 2025-01-20

# 특정 캘린더만 조회
gcalcli agenda --calendar "Work"
```

### 2. 일정 검색

```bash
# 키워드로 검색
gcalcli search "미팅"
gcalcli search "회의"
```

### 3. 일정 추가

```bash
gcalcli add --calendar "Work" \
  --when "2025-01-15 14:00" \
  --duration 60 \
  --title "팀 미팅" \
  --where "회의실 A"
```

**⚠️ 중요: 제목에 날짜/시간 포함 금지**
- ❌ "2025-01-15 14:00 팀 미팅"
- ✅ "팀 미팅"

### 4. 일정 삭제

```bash
gcalcli delete "검색어" --iamaexpert
```

---

## 📝 Daily Note 통합

Daily Note 생성 시 자동으로 일정을 가져올 수 있습니다:

```bash
gcalcli agenda --tsv
```

출력을 Markdown 리스트로 변환하여 Daily Note에 삽입합니다.

---

## 💡 캘린더 목록 확인

```bash
gcalcli list
```

---

## 🔧 트러블슈팅

### "gcalcli 명령어를 찾을 수 없습니다"
```bash
pip install gcalcli
# PATH 확인
which gcalcli
```

### "인증이 필요합니다"
```bash
gcalcli init
```

---

## 📚 참고

- gcalcli 공식: https://github.com/insanum/gcalcli
- 모든 명령어: `gcalcli --help`
