---
description: 할 일 추가
argument-hint: [할 일 내용]
allowed-tools: Write, Read, Edit
---

할 일을 추가해주세요.

**할 일**: $ARGUMENTS

**수행할 작업:**
1. `./40-personal/46-todos/active-todos.md` 파일 확인
2. 파일이 없으면 생성
3. 새 할 일 추가 (체크박스 형식)

**파일 형식:**
```markdown
# Active Todos

## 📥 Inbox (미분류)
- [ ] {새로운 할 일} (추가: YYYY-MM-DD)

## 🔥 긴급
- [ ] ...

## 📅 이번 주
- [ ] ...

## 📋 언젠가
- [ ] ...
```

**규칙:**
- 새 할 일은 "Inbox" 섹션에 추가
- 날짜 태그 자동 추가
- 완료된 항목은 `[x]`로 표시
