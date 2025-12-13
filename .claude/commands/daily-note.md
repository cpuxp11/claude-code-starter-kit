---
description: 오늘 날짜의 Daily Note 생성 또는 열기
allowed-tools: Read, Write, Edit, Bash
---

오늘 날짜의 Daily Note를 생성하거나 열어주세요.

**수행할 작업:**

1. 오늘 날짜 확인 (YYYY-MM-DD 형식)
2. 현재 워크스페이스에서 경로 확인:
   - `./40-personal/41-daily/YYYY-MM-DD.md`
3. 파일이 없으면:
   - 템플릿 읽기: `./00-system/01-templates/daily-note-template.md`
   - 변수 치환:
     - `{{date}}`: 2025-10-20
     - `{{weekday}}`: 일요일
     - `{{yesterday}}`: 2025-10-19
     - `{{tomorrow}}`: 2025-10-21
     - `{{week}}`: 2025-W42
   - 새 파일 생성
4. 파일이 있으면:
   - 현재 내용 표시

**선택 기능 (Google Calendar 연동):**

gcalcli가 설치되어 있다면 일정도 가져올 수 있습니다:
```bash
# 오늘 일정 조회
gcalcli agenda --tsv
```

일정을 Daily Note의 "스케줄" 섹션에 추가할 수 있습니다.
