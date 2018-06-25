# Decorator

Python의 코드를 보면 다음과 같은 코드들이 있다.

```python
from functools import wraps

def foo(func):
    @wraps(func)
    def decorator(*args, **kwargs):
   		return "foo"+func(*args, **wargs)
    return decorator

@foo
def bar():
    return 'bar'
```

`@foo`로 표시된 것은 `decorator`라고 하는 Python Syntax인데 이는 곧 다음과 같다.

```python
print(foo(bar())) # foobar
```

이는 Python에서 함수가 1급 객체이기 떄문에 가능하다. 함수 자체가 인자로 사용될 수 있기 때문에



데코레이터를 사용하면 많은 중복 코드를 줄일 수있으므로 적절한 곳에 잘 사용해보자.



## Refer

[PEP318 -- Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)
