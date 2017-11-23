# Git hook

Git에서 어떤 이벤트가 발생했을 때 특정 스크립트를 실행하는 기능.

`Client Hook`과 `Server Hook`으로 나뉨.

기본 훅 디렉토리는 `.git/hooks`이다.

기본적으로 쉘 스크립트로 작성된 몇가지 샘플 스크립트가 있는데 이름만 바꿔주면 바로 사용가능 하다.

스크립트는 쉘 스크립트를 포함해 `Python`, `Perl`, `Ruby` 등 스크립트 언어로 작성하면 된다.


## Client Hook

Client Hook은 `Commit Workflow Hook`, `E-mail Workflow Hook`, `ETC Client Hook` 으로 구분할 수 있다.

### Commit Workflow Hook

#### pre-commit 

커밋이 시작되면 가장 먼저 실행 되는 훅이다.

이 코드가 커밋되기 전에 확인되어야 할 것들이 있다면 이 훅을 사용한다.

`lint` 와 같이 코드 스타일을 검사한다던가, 테스트 코드를 실행 해서 잘 통과하는지 확인할 수 있다.

이 훅의 Exit 코드가 0이 아니면 커밋은 취소된다.

#### prepare-commit-msg 

이 훅은 커밋 메시지를 생성하고 편집기를 실행하기 전에 실행 된다.

커밋 메시지의 템플릿을 만들거나, 자동으로 생성하는 커밋(Merge, Squash, Amend)에 대해서 사용하면 유용하다.

이 훅은 커밋 메시지가 들어 있는 파일의 경로, 커밋의 종류를 아규먼트로 받는다.

#### commit-msg

이 훅은 최종적으로 커밋이 완료되기전에 실행된다.

커밋 메세지가 들어있는 임시파일의 경로를 아규먼트로 받는다.

이 훅의 Exit 코드가 0이 아니면 커밋은 취소된다.

#### post-commit

이 훅은 커밋이 완료되면 실행된다.

일반적으로 커밋된 것을 누군가나 어떤 프로그램에 알리기 위해 사용된다.

### E-mail Workflow Hook

#### applypatch-msg

#### pre-applypatch

#### post-applypatch


### ETC Client Hook

#### pre-rebase

`Rebase` 하기 전에 실행 된다.

이 훅의 Exit 코드가 0이 아니면 Rebase는 취소된다.

이미 Push 한 커밋은 Rebase를 못하게 할 수 있다.(sample로 들어있음)

#### post-rewrite

커밋을 번경하는 명령을 실행했을 때 실행된다.

```
$ git commit --amend
$ git rebase
```

#### post-merge

이 훅은 Merge가 되고 나서 실행된다.

Git에서 추적할 수 없는 정보를 관리하는데 사용된다.(파일 권한같이)

#### pre-push

이 훅은 Push가 되기 전에 실행 된다.

리모트의 이름, 주소를 아규먼트로 받는다.

Push 하기 전에 커밋이 유효한 커밋인지 확인하는 용도로 사용된다.

이 훅의 Exit 코드가 0이 아니면 Push는 취소된다.

#### pre-auto-gc

`git gc --auto` 명령으로 가비지 컬렉션을 실행할 수 있는데, 가비지 컬렉션이 실행 되기전에 이 훅이 실행된다.

## Server Hook

서버 훅은 모두 `Push` 이벤트의 전 후로 실행 된다.

### pre-receive 

Push 를 받으면 가장 먼저 실행된다.

Push 를 하는 Refs의 목록을 입력으로 받는다.

이 훅의 Exit 코드가 0이 아니면 Push가 취소된다.

보통 브랜치의 권한을 제어하는 용도로 사용된다.

관리자만이 브랜치를 새로 만들수 있고, 다른 개발자들은 수정사항만 Push 할 수 있게끔.

### update

`pre-receive` 와 매우 비슷하지만 한번에 브랜치를 여러 개 Push를 해도 각 브랜치 별로 한번만 실행된다.

브랜치 이름과 브랜치에서 원래 가리키고 있던 SHA-1 값, 사용자가 Push하는 SHA-1 값을 입력으로 받는다.

이 훅의 Exit 코드가 0이 아니면 Push가 취소된다.

### post-receive

이 훅은 Push 한 후에 실행된다.

보통 다른 사용자나 서비스에 알림 메세지를 보내는 용도로 사용된다.

이 스크립트가 동작하는 동안 클라이언트와 연결이 유지되고 Push를 중단시킬 수는 없다.

