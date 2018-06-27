# SQLAlchemy Query 보기

SQLAlchemy에서 ORM을 사용하다보면 실제로 어떤 Query가 실행되는 건지 궁금할 떄가 있다.

그럴때 직접 Query를 출력해볼 수 있지만 다음과 같은 방법으로 출력할 수 있다.

```python
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
```

이렇게 하면 stdout으로 어떤 쿼리가 실행되는지 출력이 되서 개발 시 도움이 많이 된다.
```
INFO:sqlalchemy.engine.base.Engine:SELECT users.email
FROM users
WHERE users.id = %s
INFO:sqlalchemy.engine.base.Engine:(1)
```

로깅 레벨을 DEBUG로 해두면 실제로 어떤 값이 넘어오는지 까지 출력된다.
