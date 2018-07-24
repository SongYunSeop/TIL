# SQLAlchemy에서 Query 로그 보기

SQLAlchemy로 ORM을 쓰다보면 실제로 어떤 Query가 수행되는지 몰라서 잘못된 패턴으로 사용할 수도 있다.(물론 거의 SQLAlchemy가 옵티마이즈 해줘서 그럴 경우는 거의 없지만...)

그래서 실제로 어떤 Query가 수행되는지 확인하는 방법을 찾다가 다음과 같은 방법을 찾았다.

## SQLAlchemy Configuring Logging

SQLAlchemy에는 4가지 logger가 있다.

- `sqlalchemy.engine` 
  레벨을 INFO로 해두면 Query를 로깅하고, DEBUG로 해두면 Query와 결과를 로깅한다.
- `sqlalchemy.dialects`
  controls custom logging for SQL dialects.(이건 아직 잘 모르겠다.)
- `sqlalchemy.pool`
  레벨을 INFO 이하로 해두면 connection pool의 checkouts/checkins 을 로깅한다.
- `sqlalchemy.orm`
  레벨을 INFO로 해두면 mapper confineration들을 로깅한다.

기본적으로 로거의 레벨은 WARNING으로 되어있다.

## Refer

- http://docs.sqlalchemy.org/en/latest/core/engines.html#configuring-logging