# HowToUse_Git
GitHub 사용법에 대해 Velog에 정리한 걸 GitHub Actions+GraphQL API를 이용한 동기화를 활용해 업로드합니다.
자세한 내용은 오른쪽에 링크된 제 velog를 통해 설명하였습니다.

## 구현 기능

- **Velog 시리즈별 포스트 동기화**: 특정 시리즈('github')의 포스트만 선택적으로 동기화
- **마크다운 형식 자동 변환**: Velog 포스트를 GitHub 마크다운 형식으로 자동 변환
- **6시간마다 자동 업데이트**: GitHub Actions를 통한 정기적인 자동 동기화 실행

<br>

## 구현 방법

- **GitHub 저장소 설정**
  - 새로운 GitHub 저장소 생성
  - GitHub Actions 권한 설정
  - Secrets 설정 (Velog 사용자명)

- **GitHub Actions 워크플로우 작성**
  - YAML 파일 작성
  - Cron 작업 스케줄링 (6시간 간격)
  - Python 환경 설정

- **Python 스크립트 작성**
  - Velog GraphQL API 연동
  - 포스트 필터링 및 변환
  - 마크다운 파일 생성
<br>

## 사용 방법

- **초기 설정 방법**
  - 저장소 Fork 또는 Clone
  - `VELOG_USERNAME` Secret 설정
  - GitHub Actions 활성화

- **자동 동기화 확인**
  - Actions 탭에서 워크플로우 실행 상태 확인
  - 동기화된 마크다운 파일 확인
  - 에러 로그 확인 방법

- **수동 동기화 방법**
  - 수동으로 워크플로우 실행하기
  - `sync_posts.py` 직접 실행하기
<br>

## 추가 커스터마이징

- **현재 적용된 커스터마이징**
  - url_slug 기반 파일명 사용으로 중복 파일 방지
  - 포스트 제목 변경 시에도 안정적인 동기화 지원

- **추가 가능한 커스터마이징**
  - 다른 시리즈 동기화 설정
  - 동기화 주기 조정
  - 마크다운 템플릿 수정
