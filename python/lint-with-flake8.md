# Lint with Flake8

> lint는 컴퓨터 프로그래밍에서 의심스럽거나, 에러를 발생하기 쉬운 코드에 표시(flag)를 달아 놓는 것을 말한다. 원래는 C 언어에서 사용하던 용어였으나 지금은 다른 언어에서도 일반적으로 사용된다. - 위키백과, 우리 모두의 백과사전.

협업을 하다보면 코딩 컨벤션의 중요성을 느끼게 된다.

코딩 컨벤션을 통일해 다수의 개발자가 코드를 수정하더라도 일관성있는 코드를 생산하는 것은 매우 중요하다.

코드 리뷰를 통해 코딩 컨벤션 체크를 할 수 있지만, 모든 커밋의 모든 코드를 매번 체크해서 컨벤션을 유지하는 것은 매우 어려운 일이다.

그래서 각 언어 별로 이를 위한 도구가 나오게 되는데 이것을 보통 Lint한다고 하는 것 같다.

## Flake8

Python 에도 당연히 Lint를 위한 도구가 존재하고 대표적으로 [`flake8`](https://pypi.python.org/pypi/flake8) 이 있다.

[PEP8](https://www.python.org/dev/peps/pep-0008/)을 기반으로 코드 컨벤션을 검사한다.

기본적인 설치와 사용법은 다음과 같다.

```bash
$ pip install flake8
$ flake8 [option] <file_name|dir_name>
```

다음과 같이 Python 코드를 작성하자.

```python
def hello():
    print 'hello'
import os
hello()
```

그리고 Lint를 실행하면 다음과 같이 메세지를 띄워준다.

```
$ flake8 test.py
test.py:3:1: E305 expected 2 blank lines after class or function definition, found 0
test.py:3:1: E402 module level import not at top of file
test.py:3:1: F401 'os' imported but unused
test.py:5:1: W391 blank line at end of file
```

Flake는 다양한 옵션과 함께 쓸수 있는데(특정 오류만 체크한다던지 등) cli에서 `--`와 옵션을 써줘서 사용하거나  
Configuration File을 만들어서 사용할 수 있다.

Configuration File 은 전역으로 사용하기 위해 User 별로 설정할 수 있다.

- Linux, OS X: `~/.config/flake8`
- Windows : `~\.flake8`

또한 각 프로젝트 별로 사용하기 위해

`setup.cfg`, `tox.ini`, `.flake8` 와 같은 파일을 사용할 수 있다.

둘 중의 하나의 방법으로 아래의 내용으로 설정 파일을 만들자.

```
[flake8]

ignore =
    E501,
    E402,
    E261

exclude = .git, __pycache__

count = True
```

이제 다시 flake8을 실행하면 메세지의 변화가 생긴다.

```
$ flake8 test.py
test.py:3:1: E305 expected 2 blank lines after class or function definition, found 0
test.py:3:1: F401 'os' imported but unused
test.py:5:1: W391 blank line at end of file
3
```

이러한 설정을 [문서](http://flake8.pycqa.org/en/latest/user/options.html)를 참고해서 작성하면 된다.

## Git Hook

Git에는 어떠한 이벤트에 특정 스크립트를 실행하는 `Hook`이라는 기능이 있다.

이 중 커밋하기 전에 실행되는 훅인 `pre-commit`에서 Lint를 하는 작업을 하게 할 수 있다.

Flake8 은 고맙게도 Git Hook을 사용해 Lint를 할 수 있는 기능을 미리 만들어뒀다.

이 기능은 Git과 Mercurial 을 지원한다.

[문서](http://flake8.pycqa.org/en/latest/user/using-hooks.html)를 보면 알겠지만 매우 간단하다.

```
$ flake8 --install-hook git
```

이 명령어를 입력하면 `.git/hooks/pre-commit` 파일이 생성된다.

`strict`, `lazy` 두 옵션을 설정해서 사용할 수 있다.

- strict

기본적으로 `false`인데 이 때는 Lint의 결과에 상관없이 커밋이 진행된다.

```
$ git config --bool flake8.strict true
```

위 처럼 true로 설정을 해두면 Lint가 실패하면(에러메세지가 하나라도 있다면) 커밋이 취소되고 메세지로 Lint 결과를 보여준다.

- lazy

기본적으로 `false`인데 이 때는 index에 올라간 코드만 검사를 한다.

lazy를 `true`로 바꾼다면 변경이 있는 파일 전체를 검사해서 Lint가 실패하면 커밋이 취소되고 메세지로 Lint 결과를 보여준다.
