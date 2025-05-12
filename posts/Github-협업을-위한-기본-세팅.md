---
title: Github 협업을 위한 기본 세팅 - branch편 
date: 2025-05-10T02:08:46.761Z
series: github
tags: branch, github, github협업, 깃허브조직
link: https://velog.io/@cheringring/Github-협업을-위한-기본-세팅
---


sw 파일럿이라는 프로젝트를 하게 되었다. 내가 경험해본 바탕으로 세팅을 적겠다. 
<br>
이 세팅은 계속 업데이트 될 예정 !
<br>

일단 Mobility3이라는 팀과 함께 조직을 구성 할 예정, 팀 셋팅하고 권한 주는 방법은 추후에 업데이트
{ ... 업데이트 ... }


![](https://velog.velcdn.com/images/cheringring/post/fdc80828-7655-4dd4-ab4e-03d1dbf3064b/image.png)

Mobility3 하위 레포에 일단 backend 레포와 curriculum 이라는 레포를 팠다.
각자 브렌치로 관리하는 게 용이 할 것 같아 브렌치를 만들어 주겠다.
<br>
### 브렌치 생성

우선 curriculum 레포에 새 브렌치를 생성해보겠다. 
<br>
#### 1. 저장소 클론 혹은 코드 스페이스 이용 

<>는 코드칠 때 생략하세요.
<br>
git clone <저장소url> 을 하거나 깃 허브 웹 페이지 코드 스페이스를 이용한다.

git clone 할 경우 :

```
git clone <저장소 url> -> cd <들어갈레포이름>
```

<br>

#### 2. 자신의 브렌치 생성

깃 클론이나 코드 스페이스를 하여 들어간 후 터미널 상에서 치면 된다.

```
git checkout -b <브렌치생성할레포이름>/<내가생성할브렌치이름>
```

<br>


#### 3. 변경 사항 커밋

```
git add . 
```

```
git commit -m "커밋내용"
```

<br>

#### 4. 브렌치 푸시

처음에 브렌치 생성할 때 하시고, 앞으로 변경 내용 푸시하실 때, 이걸 이용 하시면 됩니다.
```
git push origin <브렌치생성할레포이름>/<내가생성할브렌치이름>
```

여기서 origin은 원격 저장소를 뜻한다. 원격 저장소의 내 브렌치 레포에 푸시한다는 뜻.


<br>
<br>

### 브렌치 생성 후, 이용할 때 해야할 것.
<br>

#### 브렌치 전환

메인 브렌치를 사용하지 않고, 내 브렌치를 사용할 때 해야합니다.

```
git checkout <레포제목>/<사용할브렌치이름>
```

or

```
git switch <레포제목>/<사용할브렌치이름>
```

<br>

#### 현재 브렌치 확인

```
git branch

```

결과 예시 

![](https://velog.velcdn.com/images/cheringring/post/fc4c23d8-940f-47c9-ae8b-b6a6c3ba188a/image.png)

< * > 표시 : 내가 사용하고 있는 브렌치 

<br>

#### etc

원격 브렌치 목록 보기 

```
git branch -r
```

원격 + 로컬 브렌치 목록 보기 

```
git branch -a
```

<br><br>
각자 브렌치로 들어가셨다면 이제 폴더를 만드시면 됩니다. 
저는 과정문제를 study에 담고, 학습일지를 study_log에 담을 예정입니다. 되도록이면 폴더 이름을 통일하는 게 좋을 것 같습니다.<br>
<br>

### 각자 브렌치에서 폴더 생성

![](https://velog.velcdn.com/images/cheringring/post/5048619d-3f7e-4e74-afc2-9b556ec66972/image.png)

간단하게 Add file을 통해 깃허브 웹페이지에서 생성해 주었습니다. 
study/과정1/ex01 치시면 되시고 제일 마지막 하단이 파일이 되고, 그 전 단계는 폴더로 만들어집니다.


![](https://velog.velcdn.com/images/cheringring/post/de4281b2-57ac-4f98-b348-4afd1b78c689/image.png)

study 폴더 하단에는 이런식으로 생성해주었습니다.
과정1에 들어가면 ex01, ex02, ex03 식으로 배치 할 예정입니다. 

![](https://velog.velcdn.com/images/cheringring/post/072b8c15-c208-4ed6-b53e-23b830e934ca/image.png)


#### 주의 할 점

![](https://velog.velcdn.com/images/cheringring/post/2840b700-e54e-4d46-96d5-4241ca97105a/image.png)

풀 리퀘스트는 되도록이면 클릭하지 않도록 합시다. 승인 버튼을 누르면 main에 병합됩니다.


---
원본 포스트: https://velog.io/@cheringring/Github-협업을-위한-기본-세팅
