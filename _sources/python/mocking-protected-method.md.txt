# Protected/Private method를 Mocking 하고 싶다면?

```python
class Foo(object):

    def __far(self):
        return 'far'
```

`Foo` 클래스의 `__far` 메서드를 Mock으로 만들고 싶은데 아마도 `protected method`에는 접근하지 못하는 것 같다.

## 방법 1. 그냥 public 메서드로 감싸서 테스트한다. 

제일 빠르고 쉬운 방법이긴하다.

하지만 불필요한 코드 추가가 발생하므로 과연 좋은 방법인지...?

```python
import time
from unittest.mock import Mock

class Foo(object):

    def far(self, *args, **kwrags):
        return self.__far(*args, **kwrags)

    def __far(self):
        return time.time()

    def run(self):
        return self.far()

class TestProjectedMethod(unittest.TestCase):

    def test_Foo__far_with_public_method(self):
        foo = Foo()
        foo.far = Mock(return_value='now')
        result = foo.run()
        self.assertEqual(foo.far.call_count, 1)
        self.assertEqual(result, 'now')

```

## 방법 2. patch.object를 사용한다.

`context manager`를 사용하는 방법과 `decorator`를 사용하는 방법이 있다.

이 방법이 원래의 코드를 보존하면서 테스트를 할 수 있으므로 더 괜찮은 방법인 것 같다.

```python
import time
import unittest
from unittest.mock import Mock, patch

class Foo(object):

    def __far(self):
        return time.time()

    def run(self):
        return self.__far()

class TestProjectedMethod(unittest.TestCase):

    def test_Foo__far_with_patch_context_manager(self):
        foo = Foo()
        with patch.object(foo, '_Foo__far', return_value='now') as method:
            result = foo.run()
            self.assertEqual(method.call_count, 1)
            self.assertEqual(result, 'now')

    @patch.object(Foo, '_Foo__far', return_value='now')
    def test_Foo__far_with_patch_decorator(self, method):
        foo = Foo()
        result = foo.run()
        self.assertEqual(method.call_count, 1)
        self.assertEqual(result, 'now')
```

## 방법 3. 그리고 뭐가 있을지...?
