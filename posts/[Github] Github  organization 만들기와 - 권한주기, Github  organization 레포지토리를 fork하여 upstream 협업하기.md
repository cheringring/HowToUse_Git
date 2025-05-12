---
title: [Github] Github  organization 만들기와 
 권한주기, Github  organization 레포지토리를 fork하여 upstream 협업하기
date: 2025-05-12T08:24:18.278Z
series: github
tags: fork, github, github organization, upstream, 깃허브레포지토리, 깃허브조직, 깃허브포크
link: https://velog.io/@cheringring/Github-organization-만들기와-권한주기-Github-organization-레포지토리를-fork하여-upstream-협업하기
---


## Github  organization 만들기
1. 오른쪽 프로필을 클릭 후 your organization 클릭
![](https://velog.velcdn.com/images/cheringring/post/99eedb2a-0f01-4e65-a0c9-8a42d3a5e6d1/image.png)
2. new organization 클릭
![](https://velog.velcdn.com/images/cheringring/post/5042c830-f8cb-4fb1-b6f6-5291e8f91bc8/image.png)
그 후 plan 선택 창이 나오는데 free 로 해주심 된다. 유료 플랜 필요한 사람은 유료플랜 누르기!

3. 단체 이름과 대표 이메일 넣고 단체 소유주 넣으시면 됩니다(이때 단체 소유주는 내 깃허브 아이디)

4. Search by username, full name or email 칸에 조직에 초대해줄 사람의 유저네임이나 이메일을 쳐주면 된다. 아직 없으면 스킵!

## people 추가 
![](https://velog.velcdn.com/images/cheringring/post/bcbe618f-c12e-4269-91b1-da4df808cddd/image.png)

사람 추가하고 싶으면 invite member 해서 추가해준다. 

## Team 만들기
1. new team 해서 팀을 만들어준다.
![](https://velog.velcdn.com/images/cheringring/post/5edea4ed-5a85-4502-9110-664a0b663465/image.png)

팀을 짜주면 이 사람들이 정확히 무슨 역할을 하는지 명시적으로 알아보기 쉽겠죠?


디폴트 값으로 팀들은 owner가 만든 레포를 다 볼 수 있습니다. 

## 팀원 혹은 유저에게 해당 레포 권한 주기 
팀원들에게 특정 권한을 주고 싶으면 해당 레포 setting으로 들어갑니다.

![](https://velog.velcdn.com/images/cheringring/post/ae4a65b4-3eca-4ead-a8cf-cf1aca172651/image.png)

collaborator and teams 에 들어가셔서 add teams 혹은 add people후 권한 주고 싶은 팀/ 유저 선택 

![](https://velog.velcdn.com/images/cheringring/post/9cf91699-8c80-4417-bbbe-3a9a792f6914/image.png)

주고 싶은 권한 주기 

하지만 오픈소스 프로젝트 협업에서는 이 방법은 권장 되지 않습니다.

<br><br>

# 권장되는 팀 협업 세팅, Fork 하여 upstream

## 초기세팅

권한을 Read로 두고 Fork하는 방법이 있습니다. 원본 저장소의 원본은 그대로 유지되며, 풀 리퀘스트를 통해 통합 할 수 있습니다.

<br>

1. 우측 상단에 fork 클릭 

![](https://velog.velcdn.com/images/cheringring/post/25884a22-51b0-456a-b54d-fbca8c08ad32/image.png)

<br>

2. fork 할때 copy the main branch only 체크 해제 

![](https://velog.velcdn.com/images/cheringring/post/094fc704-c4fe-4d70-be28-27068556fc18/image.png)


3. 내 저장소에 포크됨.
![](https://velog.velcdn.com/images/cheringring/post/9e9a638d-ecf2-4147-b20c-d8f70a8e9d7d/image.png)

<br>

4. Fork된 본인 저장소를 로컬로 클론
```
git clone https://github.com/[본인계정]/[저장소이름].git
cd [저장소이름]
```

5. 원본 저장소를 upstream으로 추가

```
git remote add upstream https://github.com/[조직명]/[저장소이름].git
```

<br>
<br>

## 새로운 작업 시작할 때마다 실행
<br>

#### 1. 메인 브렌치로 이동 
```
git checkout main
```

#### 2.  원본 저장소의 최신 변경사항 가져오기
```
git fetch upstream
git merge upstream/main
```

#### # 3. 새로운 브랜치 생성 (작업 내용을 이름으로 사용)
```
git checkout -b feature/login    # 예: 로그인 기능 개발
```

주요 브랜치 접두어 컨벤션:
- feature/ : 새로운 기능 개발
- fix/ : 버그 수정
- docs/ : 문서 작업
- refactor/ : 코드 개선/리팩토링

<br>
<br>


## 코드 작업 및 커밋

<br>

 #### 1. 파일 수정 후 변경사항 확인
```
 git status
```

####  2. 변경된 파일들 스테이징
```
git add . (전부)

or 

git add <file1> <file2> (file1,2를 add)
```

#### 3. 커밋하기

```
git commit -m "로그인 기능 구현"
```

#### 4. 본인의 Fork된 저장소에 변경사항 Push하기

```
git push origin feature/login
```
<br>

#### 5. Pull Request 생성
<br>

1. GitHub의 Fork된 저장소 페이지 방문
<br>

2. Compare & pull request 버튼 클릭
   (또는 Pull requests 탭 → New pull request)
   <br>


3. PR 내용 작성
  - 제목: 작업 내용 간단히 설명
   - 본문: 상세 설명, 관련 이슈 번호 등
   - 리뷰어 지정
   - 라벨 추가
<br>
4. Create pull request 클릭

-> owner가 승인하면 병합됨.

<br><br>

## 리뷰 후 수정 요청받은 경우

#### 1. 수정 요청 받은 브랜치에서 파일 수정 

#### 2. 변경사항 커밋
git add .
git commit -m "리뷰 반영: 로그인 유효성 검사 추가"

#### 3. 다시 Push
git push origin feature/login



## PR 병합 후 정리 

#### 1. 로컬에서 main 브랜치로 이동
git checkout main

#### 2. 로컬에서 더 이상 필요없는 브랜치 삭제
git branch -d feature/login

#### 3. 원본 저장소(조직)의 변경사항을 로컬로 가져오기
git fetch upstream
git merge upstream/main

#### 4. 로컬의 변경사항을 포크된 저장소(본인 계정)에 올리기
git push origin main


이러면 깔끔하게 관리가 됩니다~! 

헷갈릴수도 있는데 지금 내 컴퓨터 로컬은 내 개인 저장소(조직 레포를 포크한)을 클론한겁니다.


---
원본 포스트: https://velog.io/@cheringring/Github-organization-만들기와-권한주기-Github-organization-레포지토리를-fork하여-upstream-협업하기
