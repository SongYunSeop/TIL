# Python에서 public, protected, private

Object Oriended Programming에서는 3가지 접근권한이 있다.

- Public
- Protected
- Private

이런 접근 권한을 설정하고 클래스 내부나 클래스 외부 혹은 상속받은 클래스에서 메서드나 변수에 접근할 수 있는가를 결정한다.

하지만 Python에서는 이런 접근 권한이 `C++`이나 `Java` 처럼 강제적이지 않고, **Protected Property 나 Private Property에도 접근할 수 있으나 되도록이면 그렇게 사용하지 맙시다** 라는 암묵적인 규칙이 있다. ~~하지만 하지말라면 하고싶은 것이 인간의 본능이지~~

자유로운 Pythonic 정신이 이런 것을 가능하게 했다. [PEP-8](https://www.python.org/dev/peps/pep-0008/#method-names-and-instance-variables)에 `Method Names and Instance Variables` 라는 섹션을 참고

## Public

기본적으로 아무런 표시를 하지 않는다면 Public method, Public property로 사용한다.

```python
class PublicUser:
    def __init__(self, name):
        self.name = name

public_user = PublicUser('yunseop')
print public_user.name # yunseop
```

## Protected

 언더바 한개(`_`)를 붙여주면 Protected method, Protected property로 사용한다.

```python
class ProtectedUser:
    def __init__(self, name):
        self._name = name

protected_user = ProtectedUser('yunseop')
print protected_user._name # yunseop
```

## Private

언더바 두개(`__`)를 붙여주면 Private method, Private property로 사용한다.

```python
class PrivateUser:
    def __init__(self, name):
        self.__name = name
        
private_user = PrivateUser('yunseop')
print private._PrivateUser__name # yunseop
```

