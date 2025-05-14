---
title: Velog 포스트 자동 백업하기(특정 시리즈) - GitHub Actions로 구현하는 GraphQL API를 이용한 동기화 
date: 2025-05-12T09:15:01.368Z
series: github
tags: GithubAction, Velog자동백업, githubvelog, graphql, veloggithub
link: https://velog.io/@cheringring/Velog-특정-카테고리-글을-GitHub-레파지토리에-올리기
---


하고 싶어서 찾아봤더니 아무도 한 사람이 없어서 구현해보는 ... 
<br>

1. 구현 기능
   - Velog 시리즈별 포스트 동기화
   - 마크다운 형식 자동 변환
   - 6시간마다 자동 업데이트

2. 구현 방법
   - GitHub 저장소 설정
   - GitHub Actions 워크플로우 작성
   - Python 스크립트 작성

3. 사용 방법
   - 초기 설정 방법
   - 자동 동기화 확인
   - 수동 동기화 방법

4. 추가 커스터마이징
   - 다른 시리즈 동기화
   - 동기화 주기 변경
   - 마크다운 형식 수정
   
   <br>
   <br>
   
### 1. 원본 저장소 생성 
![](https://velog.velcdn.com/images/cheringring/post/83efc03a-d5d2-4fe5-9520-6d7168a56763/image.png)
<br>

### 2. git clone <저장소 명> or codespace 들어감.
git clone 할 시 
```
git clone <저장소 명>
cd <저장소 명>
```

<br><br>

### 3. .github/workflows 디렉토리 생성

```
mkdir -p .github/workflows
```

<br><br>

#### 4. .github/workflows/velog-sync.yml 파일 작성 

![](https://velog.velcdn.com/images/cheringring/post/758b975b-8c34-4200-815c-ea42d48c620b/image.png)

<br>

#### 5. 특정 시리즈 동기화 스크립트 작성


![](https://velog.velcdn.com/images/cheringring/post/dc6f9e3a-d662-47ca-bc6b-3092e78dcb1c/image.png)

![](https://velog.velcdn.com/images/cheringring/post/545d5ff2-79a3-4e82-884e-358312dc4935/image.png)

![](https://velog.velcdn.com/images/cheringring/post/1b4866fa-2469-4027-8041-fa99e0feaf6a/image.png)



이렇게 되면 내가 쓴 velog 이름대로 posts 폴더에 .md 형태로 저장된다 

<br>

###  디렉토리 구조 
![](https://velog.velcdn.com/images/cheringring/post/960c9bbd-b50a-40d0-89d9-8d028794a04c/image.png)

<br>
<br>
<br>

### GitHub Actions 실행 확인

####  1. GitHub 저장소의 Actions 탭 -> 좌측 Sync Velog GitHub Series Posts 워크플로우 확인  
![](https://velog.velcdn.com/images/cheringring/post/65774c44-6075-4303-a9a2-5f3a791d9dee/image.png)

Sync Velog~ 클릭 후 Run workflow


![](https://velog.velcdn.com/images/cheringring/post/5abec2e5-2525-4e33-9ebf-1cfc6e66f5e5/image.png)
run 완료한 화면

sync Velog GitHub Series Posts 액션 클릭하면 
![](https://velog.velcdn.com/images/cheringring/post/2af51d5c-087b-4088-83b7-ca7d1121cfdd/image.png)

이런 창이 뜨는데 

![](https://velog.velcdn.com/images/cheringring/post/e071afc3-fa4a-4176-9888-1b9bb8a68d33/image.png)

Syns Posts에 이런 화면이 뜨면 완전하게 된거다. 
후후 


##  Actions 권한 설정 확인
#### 1. 저장소 Settings → Actions → General
#### 2. Workflow permissions에서 Read and write permissions 선택하고 Save


<br><br>
12차 시도만에 했습니다. git commit이랑 push 무진장함 ㅎㅎ 
log보면서 계속 뜯어 고쳤네요.

![](https://velog.velcdn.com/images/cheringring/post/fc02ae6a-66b2-4750-90fc-67c9ceed43f4/image.png)



<br>
짠 !

![](https://velog.velcdn.com/images/cheringring/post/5325e9ee-1b33-40c1-b7d8-54e98f42cf6c/image.png)

이렇게 완전히 스크래핑 된 화면을 볼 수 있다.
아주 유용하게 쓰고 있어서 기분이 좋다.


> 코드를 보시다시피 6시간마다 자동으로 동기화 되고, 그냥 업로딩 하고 싶으면 Action들어가셔서 workflow 클릭하시면 posts 에 md 형식으로 마크다운 되어 있을겁니다.<br>
깃허브 Posts 디렉토리 안에 표시되는 .md 제목은 벨로그 링크 주소 이름이 표시됩니다. <br>
원래 제목으로 했는데 이렇게 하는 이유는 URL slug는 고유하고 안정적이고, 특수문자나 공백이 없어 파일 시스템에 안전합니다. <br>
그리고 가장 큰 이유는 포스트의 제목이 변경되어도 동일한 파일을 유지할 수 있습니다.





---
원본 포스트: https://velog.io/@cheringring/Velog-특정-카테고리-글을-GitHub-레파지토리에-올리기
