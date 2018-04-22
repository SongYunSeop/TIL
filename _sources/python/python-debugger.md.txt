# Python Debugger

개발할 때 Python Debugger, `pdb` 를 많이 쓰곤한다.

아래와 같이 코드상에서 브레이크 포인트를 지정할 수 있다.

```python
def hello():
    import pdb; pdb.set_trace()
    print 'Hello, World!'

hello()
```

그리고 스크립트를 실행하면 저 포인트에서 여러가지 기능을 사용해 디버깅을 할 수 있다.

```bash
$ python test.py
> /Users/sys/workspace/test.py(3)hello()
-> print 'Hello, World!'
(Pdb)
```

여러가지 명령어 중 많이 쓰는 명령어는 다음과 같다.

- `c(ontinue)`: 다음 브레이크 포인트까지 실행. 브레이크 포인트가 없다면 계속 실행.

- 'n(ext)': 다음 1 라인 실행.

- 'l(ist)`: 현재 파일의 코드를 프린트함.

- 'a(rgs)`: 함수의 인자들을 프린트함.
