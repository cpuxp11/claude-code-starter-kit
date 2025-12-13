---
description: 워크스페이스 초기 설정 마법사
allowed-tools: Write, Read, Bash, Edit
---

Claude Code 워크스페이스 초기 설정을 진행합니다.

**수행할 작업:**

## 1. 환영 메시지
```
🎉 Claude Code Starter Kit에 오신 것을 환영합니다!

이 설정 마법사가 워크스페이스를 초기화해드립니다.
```

## 2. 사용자 정보 수집
- 이름 (Daily Note 등에 사용)
- 주요 사용 목적 (프로젝트 관리 / 지식 관리 / 일기 / 기타)

## 3. 폴더 구조 확인
현재 Johnny Decimal 구조가 올바른지 확인:
- `00-inbox/` 존재 확인
- `40-personal/41-daily/` 존재 확인
- `00-system/01-templates/` 존재 확인

## 4. 첫 Daily Note 생성
```
첫 번째 Daily Note를 생성할까요? (Y/n)
```

## 5. 완료 메시지
```
✅ 설정 완료!

사용 가능한 명령어:
- /daily-note  : 오늘 노트 생성
- /idea        : 아이디어 저장
- /todo        : 할 일 추가
- /todos       : 할 일 목록
- /crawl       : 웹페이지 크롤링 (설정 필요)

💡 팁: 매일 /daily-note로 하루를 시작해보세요!
```

## 6. 다음 단계 안내
- Google Calendar 연동: gcalcli 설치 필요
- 웹 크롤링: Python 환경 설정 필요
