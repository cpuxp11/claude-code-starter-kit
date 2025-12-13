---
description: 새로운 커스텀 슬래시 명령어 생성
argument-hint: [명령어 이름]
allowed-tools: Write, Read
---

새로운 슬래시 명령어를 생성합니다.

**명령어 이름**: $ARGUMENTS

**수행할 작업:**

1. 사용자에게 다음 정보 요청:
   - 명령어 설명 (한 줄)
   - 명령어가 수행할 작업
   - 필요한 도구 (Read, Write, Edit, Bash 중)
   - 인자 필요 여부

2. `.claude/commands/{명령어이름}.md` 파일 생성

**템플릿:**
```markdown
---
description: {한 줄 설명}
argument-hint: [{인자 설명}]  # 인자가 필요한 경우만
allowed-tools: {도구 목록}
---

{명령어 설명}

**수행할 작업:**
1. {단계 1}
2. {단계 2}
3. ...

**참고:**
- {주의사항이나 팁}
```

**예시:**
- `/daily-note` - 매일 노트 생성
- `/idea` - 아이디어 저장
- `/crawl` - 웹페이지 크롤링
