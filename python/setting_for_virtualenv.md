# Virtualenv Setting

virtualenv없이 python을 쓴다는건 상상도 못할만큼 좋은 툴이다.

독립적인 개발 환경을 만들어주므로 각 프로젝트 별로 라이브러리의 충돌을 방지할 수 있다.

## 설치

우선 pip가 설치되었는지 확인하자.

```bash
$ pip -V
pip 9.0.1 from /usr/local/lib/python2.7/site-packages (python 2.7)
```

그리고 virtualenv를 설치하는데 더욱 편리한 사용을 위해 virtualenvwrapper도 같이 설치해주자.

```bash
$ pip install virtualenv virtualenvwrapper
...
Successfully installed virtualenv ...
```

성공적으로 설치가 되면 `WORKON_HOME`이라는 환경변수에 virtualenv가 담길 위치를  설정해주자.

```bash
$ export WORKON_HOME=~/.envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
```

그러면 설정은 완료되고 이제 사용하면 된다.

## 사용방법

```bash
mkvirtualenv <env_name>         make virtualenv
rmvirtualenv <env_name>         remove virtualenv
workon                          show virtualenv list
workon <env_name>               activate virtualenv
deactivate                      deactivate virtualenv
```


